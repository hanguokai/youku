"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from .util import check_error, remove_none_value


class YoukuVideos(object):

    """Youku Videos API.

    doc:http://open.youku.com/docs/api_videos.html
    """

    def __init__(self, client_id):
        super(YoukuVideos, self).__init__()
        self.client_id = client_id

    def find_video_by_id(self, video_id):
        """doc: http://open.youku.com/docs/doc?id=44
        """
        url = 'https://openapi.youku.com/v2/videos/show_basic.json'
        params = {
            'client_id': self.client_id,
            'video_id': video_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_video_by_url(self, video_url):
        """doc: http://open.youku.com/docs/doc?id=44
        """
        url = 'https://openapi.youku.com/v2/videos/show_basic.json'
        params = {
            'client_id': self.client_id,
            'video_url': video_url
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_videos_by_ids(self, video_ids):
        """doc: http://open.youku.com/docs/doc?id=45
        """
        url = 'https://openapi.youku.com/v2/videos/show_basic_batch.json'
        params = {
            'client_id': self.client_id,
            'video_ids': video_ids
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_video_detail_by_id(self, video_id, ext=None):
        """doc: http://open.youku.com/docs/doc?id=46
        """
        url = 'https://openapi.youku.com/v2/videos/show.json'
        params = {
            'client_id': self.client_id,
            'video_id': video_id
        }
        if ext:
            params['ext'] = ext
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_video_details_by_ids(self, video_ids, ext=None):
        """doc: http://open.youku.com/docs/doc?id=47
        """
        url = 'https://openapi.youku.com/v2/videos/show_batch.json'
        params = {
            'client_id': self.client_id,
            'video_ids': video_ids
        }
        if ext:
            params['ext'] = ext
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_videos_by_me(self, access_token, orderby='published',
                          page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=48
        """
        url = 'https://openapi.youku.com/v2/videos/by_me.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_videos_by_userid(self, user_id, orderby='published',
                              page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=49
        """
        url = 'https://openapi.youku.com/v2/videos/by_user.json'
        params = {
            'client_id': self.client_id,
            'user_id': user_id,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_videos_by_username(self, user_name, orderby='published',
                                page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=49
        """
        url = 'https://openapi.youku.com/v2/videos/by_user.json'
        params = {
            'client_id': self.client_id,
            'user_name': user_name,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def update_video(self, access_token, video_id, title=None,
                     tags=None, category=None, copyright_type=None,
                     public_type=None, watch_password=None,
                     description=None, thumbnail_seq=None):
        """doc: http://open.youku.com/docs/doc?id=50
        """
        url = 'https://openapi.youku.com/v2/videos/update.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'video_id': video_id,
            'title': title,
            'tags': tags,
            'category': category,
            'copyright_type': copyright_type,
            'public_type': public_type,
            'watch_password': watch_password,
            'description': description,
            'thumbnail_seq': thumbnail_seq
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def destroy_video(self, access_token, video_id):
        """doc: http://open.youku.com/docs/doc?id=51
        """
        url = 'https://openapi.youku.com/v2/videos/destroy.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'video_id': video_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def find_videos_by_related(self, video_id, count=20):
        """doc: http://open.youku.com/docs/doc?id=52
        """
        url = 'https://openapi.youku.com/v2/videos/by_related.json'
        params = {
            'client_id': self.client_id,
            'video_id': video_id,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_favorite_videos_by_me(self, access_token, orderby='favorite-time',
                                   page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=53
        """
        url = 'https://openapi.youku.com/v2/videos/favorite/by_me.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_favorite_videos_by_userid(self, user_id,
                                       orderby='favorite-time',
                                       page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=54
        """
        url = 'https://openapi.youku.com/v2/videos/favorite/by_user.json'
        params = {
            'client_id': self.client_id,
            'user_id': user_id,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_favorite_videos_by_username(self, user_name,
                                         orderby='favorite-time',
                                         page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=54
        """
        url = 'https://openapi.youku.com/v2/videos/favorite/by_user.json'
        params = {
            'client_id': self.client_id,
            'user_name': user_name,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def create_favorite_video(self, access_token, video_id):
        """doc: http://open.youku.com/docs/doc?id=55
        """
        url = 'https://openapi.youku.com/v2/videos/favorite/create.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'video_id': video_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def destroy_favorite_video(self, access_token, video_id):
        """doc: http://open.youku.com/docs/doc?id=56
        """
        url = 'https://openapi.youku.com/v2/videos/favorite/destroy.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'video_id': video_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def find_videos_by_category(self, category, genre=None,
                                period='today',
                                orderby='view-count',
                                page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=57
        """
        url = 'https://openapi.youku.com/v2/videos/by_category.json'
        params = {
            'client_id': self.client_id,
            'category': category,
            'period': period,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        if genre:
            params['genre'] = genre
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
