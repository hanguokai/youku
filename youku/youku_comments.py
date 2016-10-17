"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from .util import check_error, remove_none_value


class YoukuComments(object):

    """Youku Comments API. Not yet implemented.

    doc: http://open.youku.com/docs/api_comments.html
    """

    def __init__(self, client_id):
        super(YoukuComments, self).__init__()
        self.client_id = client_id

    def find_comment_by_id(self, comment_id):
        """doc: http://open.youku.com/docs/doc?id=32
        """
        url = 'https://openapi.youku.com/v2/comments/show.json'
        params = {
            'client_id': self.client_id,
            'comment_id': comment_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_comments_by_ids(self, comment_ids):
        """doc: http://open.youku.com/docs/doc?id=34
        """
        url = 'https://openapi.youku.com/v2/comments/show_batch.json'
        params = {
            'client_id': self.client_id,
            'comment_ids': comment_ids
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_comments_by_video(self, video_id, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=35
        """
        url = 'https://openapi.youku.com/v2/comments/by_video.json'
        params = {
            'client_id': self.client_id,
            'video_id': video_id,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_hot_comments_by_video(self, video_id, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=36
        """
        url = 'https://openapi.youku.com/v2/comments/hot/by_video.json'
        params = {
            'client_id': self.client_id,
            'video_id': video_id,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_comments_by_me(self, access_token, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=37
        """
        url = 'https://openapi.youku.com/v2/comments/by_me.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'page': page,
            'count': count
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def find_comments_by_mention_me(self, access_token, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=38
        """
        url = 'https://openapi.youku.com/v2/comments/by_mention_me.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'page': page,
            'count': count
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def find_comments_by_reply_me(self, access_token, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=39
        """
        url = 'https://openapi.youku.com/v2/comments/by_reply_me.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'page': page,
            'count': count
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def find_comments_by_to_me(self, access_token, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=40
        """
        url = 'https://openapi.youku.com/v2/comments/to_me.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'page': page,
            'count': count
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def create_comment(self, access_token, video_id, content,
                       reply_id=None, captcha_key=None, captcha_text=None):
        """doc: http://open.youku.com/docs/doc?id=41
        """
        url = 'https://openapi.youku.com/v2/comments/create.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'video_id': video_id,
            'content': content,
            'reply_id': reply_id,
            'captcha_key': captcha_key,
            'captcha_text': captcha_text
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def destroy_comment(self, access_token, comment_id):
        """doc: http://open.youku.com/docs/doc?id=42
        """
        url = 'https://openapi.youku.com/v2/comments/destroy.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'comment_id': comment_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']
