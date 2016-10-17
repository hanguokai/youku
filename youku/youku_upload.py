"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/doc?id=110
"""

import os
import requests
import json
import hashlib
import logging
import socket
from time import sleep
from .util import check_error, YoukuError


class YoukuUpload(object):

    """Youku Upload Client.

    Upload file to Youku Video. Support resume upload if interrupted.
    Should use one instance of YoukuUpload for one upload file in one thread,
    since it has internal state of upload process.

    doc: http://open.youku.com/docs/doc?id=110
    """

    def __init__(self, client_id, access_token, file, logger=None):
        """
        Args:
            file: string, include path and filename for open(). filename
                must contain video file extension.
        """
        super(YoukuUpload, self).__init__()
        self.client_id = client_id
        self.access_token = access_token
        self.logger = logger or logging.getLogger(__name__)

        # file info
        self.file = file
        self.file_size = os.path.getsize(self.file)  # int
        self.file_dir, self.file_name = os.path.split(self.file)  # string
        if self.file_dir == '':
            self.file_dir = '.'
        self.file_ext = self.file_name.rsplit('.', 1)[1],  # file extension
        self.file_md5 = None  # string, do later

        # upload state
        self.upload_token = None  # string
        self.upload_server_ip = None  # string
        self.slice_task_id = None  # int
        self.slice_offset = None  # int
        self.slice_length = None  # int
        self.transferred = None  # int for bytes has uploaded
        self.finished = False  # boolean

        # resume upload state
        self._read_upload_state_from_file()

    def prepare_video_params(self, title=None, tags='Others', description='',
                             copyright_type='original', public_type='all',
                             category=None, watch_password=None,
                             latitude=None, longitude=None, shoot_time=None
                             ):
        """ util method for create video params to upload.

        Only need to provide a minimum of two essential parameters:
        title and tags, other video params are optional. All params spec
        see: http://open.youku.com/docs/upload_client_chinese.html#create .

        Args:
            title: string, 2-50 characters.
            tags: string, 1-10 tags joind with comma.
            description: string, less than 2000 characters.
            copyright_type: string, 'original' or 'reproduced'
            public_type: string, 'all' or 'friend' or 'password'
            watch_password: string, if public_type is password.
            latitude: double.
            longitude: double.
            shoot_time: datetime.

        Returns:
            dict params that upload/create method need.
        """
        params = {}
        if title is None:
            title = self.file_name
        elif len(title) > 80:
            title = title[:80]

        if len(description) > 2000:
            description = description[0:2000]

        params['title'] = title
        params['tags'] = tags
        params['description'] = description
        params['copyright_type'] = copyright_type
        params['public_type'] = public_type
        if category:
            params['category'] = category
        if watch_password:
            params['watch_password'] = watch_password
        if latitude:
            params['latitude'] = latitude
        if longitude:
            params['longitude'] = longitude
        if shoot_time:
            params['shoot_time'] = shoot_time

        return params

    def create(self, params):
        # prepare file info
        params['file_name'] = self.file_name
        params['file_size'] = self.file_size
        params['file_md5'] = self.file_md5 = self.checksum_md5file(self.file)
        self.logger.info('upload file %s, size: %d bytes' %
                         (self.file_name, self.file_size))
        self.logger.info('md5 of %s: %s' %
                         (self.file_name, self.file_md5))

        params['client_id'] = self.client_id
        params['access_token'] = self.access_token

        url = 'https://openapi.youku.com/v2/uploads/create.json'
        r = requests.get(url, params=params)
        check_error(r, 201)
        result = r.json()

        self.upload_token = result['upload_token']
        self.logger.info('upload token of %s: %s' %
                         (self.file_name, self.upload_token))

        if result['instant_upload_ok'] == 'yes':
            # pass upload and finish
            # this case hasn't happen and test
            self.logger.info("instant upload %s" % self.file_name)
            return self.commit()

        self.upload_server_ip = socket.gethostbyname(
            result['upload_server_uri'])
        self.logger.info('upload_server_ip of %s: %s' %
                         (self.file_name, self.upload_server_ip))

    def _save_upload_state_to_file(self):
        """if create and create_file has execute, save upload state
        to file for next resume upload if current upload process is
        interrupted.
        """
        if os.access(self.file_dir, os.W_OK | os.R_OK | os.X_OK):
            save_file = self.file + '.upload'
            data = {
                'upload_token': self.upload_token,
                'upload_server_ip': self.upload_server_ip
            }
            with open(save_file, 'w') as f:
                json.dump(data, f)

    def _read_upload_state_from_file(self):
        save_file = self.file + '.upload'
        try:
            with open(save_file) as f:
                data = json.load(f)
                self.upload_token = data['upload_token']
                self.upload_server_ip = data['upload_server_ip']
                # check upload_token expired
                try:
                    self.check()
                except YoukuError as e:
                    if e.code == 120010223:
                        # Expired upload token
                        self.upload_token = None
                        self.upload_server_ip = None
                        self._delete_upload_state_file()
        except:
            pass

    def _delete_upload_state_file(self):
        try:
            os.remove(self.file + '.upload')
        except:
            pass

    def checksum_md5file(self, filename):
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()

    def checksum_md5data(self, data):
        md5 = hashlib.md5()
        md5.update(data)
        return md5.hexdigest()

    def create_file(self):
        params = {
            'upload_token': self.upload_token,
            'file_size': self.file_size,  # Byte
            'ext': self.file_ext,
            'slice_length': 2048  # KB
        }
        url = 'http://%s/gupload/create_file' % self.upload_server_ip
        r = requests.post(url, data=params)
        check_error(r, 201)

        # save upload state to resume upload
        self._save_upload_state_to_file()

    def new_slice(self):
        params = {
            'upload_token': self.upload_token
        }
        url = 'http://%s/gupload/new_slice' % self.upload_server_ip
        r = requests.get(url, params=params)
        check_error(r, 201)
        self._save_slice_state(r.json())

    def _save_slice_state(self, result):
        self.slice_task_id = result['slice_task_id']
        self.slice_offset = result['offset']
        self.slice_length = result['length']
        self.transferred = result['transferred']
        self.finished = result['finished']

    def upload_slice(self):
        data = None
        with open(self.file, 'rb') as f:
            f.seek(self.slice_offset)
            data = f.read(self.slice_length)
        params = {
            'upload_token': self.upload_token,
            'slice_task_id': self.slice_task_id,
            'offset': self.slice_offset,
            'length': self.slice_length,  # Byte
            'hash': self.checksum_md5data(data)
        }
        url = 'http://%s/gupload/upload_slice' % self.upload_server_ip
        r = requests.post(url, params=params, data=data)
        check_error(r, 201)
        self._save_slice_state(r.json())

    def check(self):
        params = {
            'upload_token': self.upload_token
        }
        url = 'http://%s/gupload/check' % self.upload_server_ip
        r = requests.get(url, params=params)
        check_error(r, 200)
        return r.json()

    def commit(self):
        status = self.check()
        if status['status'] == 4:
            raise ValueError('upload has not complete, should not commit')
        while status['status'] != 1:  # status is 2 or 3
            sleep(10)
            status = self.check()

        params = {
            'access_token': self.access_token,
            'client_id': self.client_id,
            'upload_token': self.upload_token,
            'upload_server_ip': status['upload_server_ip']
        }
        url = 'https://openapi.youku.com/v2/uploads/commit.json'
        r = requests.post(url, data=params)
        check_error(r, 200)
        self.finished = True
        self._delete_upload_state_file()
        return r.json()['video_id']

    def cancel(self):
        status = self.check()
        params = {
            'access_token': self.access_token,
            'client_id': self.client_id,
            'upload_token': self.upload_token,
            'upload_server_ip': status['upload_server_ip']
        }
        url = 'https://openapi.youku.com/v2/uploads/cancel.json'
        r = requests.get(url, params=params)
        check_error(r, 200)
        self._delete_upload_state_file()
        return r.json()['upload_token']

    def spec(self):
        url = 'https://openapi.youku.com/v2/schemas/upload/spec.json'
        r = requests.get(url)
        check_error(r, 200)
        return r.json()

    def transferred_percent(self):
        """return current transferred percent
        """
        return int(self.transferred / self.file_size)

    def upload(self, params={}):
        """start uploading the file until upload is complete or error.
           This is the main method to used, If you do not care about
           state of process.

           Args:
                params: a dict object describe video info, eg title,
                tags, description, category.
                all video params see the doc of prepare_video_params.

           Returns:
                return video_id if upload successfully
        """
        if self.upload_token is not None:
            # resume upload
            status = self.check()
            if status['status'] != 4:
                return self.commit()
            else:
                self.new_slice()
                while self.slice_task_id != 0:
                    self.upload_slice()
                return self.commit()
        else:
            # new upload
            self.create(self.prepare_video_params(**params))
            self.create_file()
            self.new_slice()
            while self.slice_task_id != 0:
                self.upload_slice()
            return self.commit()
