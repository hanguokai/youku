"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from util import check_error, remove_none_value


class YoukuUsers(object):

    """Youku Users API.

    doc: http://open.youku.com/docs/api_users.html
    """

    def __init__(self, client_id):
        super(YoukuUsers, self).__init__()
        self.client_id = client_id

    def my_info(self, access_token):
        """doc: http://open.youku.com/docs/doc?id=23
        """
        url = 'https://openapi.youku.com/v2/users/myinfo.json'
        data = {'client_id': self.client_id,
                'access_token': access_token}
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def find_user_by_id(self, user_id):
        """doc: http://open.youku.com/docs/doc?id=24
        """
        return self._find_user(user_id=user_id)

    def find_user_by_name(self, user_name):
        """doc: http://open.youku.com/docs/doc?id=24
        """
        return self._find_user(user_name=user_name)

    def find_users_by_ids(self, user_ids):
        """doc: http://open.youku.com/docs/doc?id=25
        """
        return self._find_users(user_ids=user_ids)

    def find_users_by_names(self, user_names):
        """doc: http://open.youku.com/docs/doc?id=25
        """
        return self._find_users(user_names=user_names)

    def _find_user(self, user_id=None, user_name=None):
        url = 'https://openapi.youku.com/v2/users/show.json'
        data = {
            'client_id': self.client_id,
            'user_id': user_id,
            'user_name': user_name
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        if r.status_code == 400:
            # Youku return 400 if no result, but this is not friendly.
            return None
        check_error(r)
        return r.json()

    def _find_users(self, user_ids=None, user_names=None):
        url = 'https://openapi.youku.com/v2/users/show_batch.json'
        data = {
            'client_id': self.client_id,
            'user_ids': user_ids,
            'user_names': user_names
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        if r.status_code == 400:
            # Youku return 400 if no result, but this is not friendly.
            return None
        check_error(r)
        return r.json()

    def friendship_followings(self, user_id=None, user_name=None,
                              page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=26
        """
        url = 'https://openapi.youku.com/v2/users/friendship/followings.json'
        data = {
            'client_id': self.client_id,
            'page': page,
            'count': count,
            'user_id': user_id,
            'user_name': user_name
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def friendship_followers(self, user_id=None, user_name=None,
                             page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=27
        """
        url = 'https://openapi.youku.com/v2/users/friendship/followers.json'
        data = {
            'client_id': self.client_id,
            'page': page,
            'count': count,
            'user_id': user_id,
            'user_name': user_name
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def create_friendship(self, access_token,
                          user_id=None, user_name=None):
        """doc: http://open.youku.com/docs/doc?id=28
        """
        url = 'https://openapi.youku.com/v2/users/friendship/create.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'user_id': user_id,
            'user_name': user_name
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def destroy_friendship(self, access_token,
                           user_id=None, user_name=None):
        """doc: ??
        """
        url = 'https://openapi.youku.com/v2/users/friendship/destroy.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'user_id': user_id,
            'user_name': user_name
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def create_subscribe(self, access_token, show_id):
        """doc: http://open.youku.com/docs/doc?id=29
        """
        url = 'https://openapi.youku.com/v2/users/subscribe/create.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token,
            'show_id': show_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()['result'] == 0

    def cancel_subscribe(self, access_token, show_id):
        """doc: ??
        """
        url = 'https://openapi.youku.com/v2/users/subscribe/cancel.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token,
            'show_id': show_id
        }
        r = requests.post(url, data=params)
        check_error(r)
        return r.json()['result'] == 0

    def subscribe_get(self, access_token, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=30
        """
        url = 'https://openapi.youku.com/v2/users/subscribe/get.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def subscribe_notice(self, access_token):
        """doc: http://open.youku.com/docs/doc?id=31
        """
        url = 'https://openapi.youku.com/v2/users/subscribe/notice.json'
        params = {
            'client_id': self.client_id,
            'access_token': access_token
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
