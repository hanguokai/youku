"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from .util import check_error, remove_none_value


class YoukuPlaylists(object):

    """Youku Playlists API.

    doc: http://open.youku.com/docs/api_playlists.html
    """

    def __init__(self, client_id):
        super(YoukuPlaylists, self).__init__()
        self.client_id = client_id

    def find_playlist_by_id(self, playlist_id):
        """doc: http://open.youku.com/docs/doc?id=66
        """
        url = 'https://openapi.youku.com/v2/playlists/show.json'
        params = {
            'client_id': self.client_id,
            'playlist_id': playlist_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_playlists_by_ids(self, playlist_ids):
        """doc: http://open.youku.com/docs/doc?id=67
        """
        url = 'https://openapi.youku.com/v2/playlists/show_batch.json'
        params = {
            'client_id': self.client_id,
            'playlist_ids': playlist_ids
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_playlists_by_category(self, category, period='today',
                                   orderby='published', page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=68
        """
        url = 'https://openapi.youku.com/v2/playlists/by_category.json'
        params = {
            'client_id': self.client_id,
            'category': category,
            'period': period,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_playlists_by_me(self, access_token,
                             orderby='published', page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=69
        """
        url = 'https://openapi.youku.com/v2/playlists/by_me.json'
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

    def find_playlists_by_userid(self, user_id,
                                 orderby='published', page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=70
        """
        url = 'https://openapi.youku.com/v2/playlists/by_user.json'
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

    def find_playlists_by_username(self, user_name,
                                   orderby='published', page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=70
        """
        url = 'https://openapi.youku.com/v2/playlists/by_user.json'
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

    def find_videos_by_playlist(self, playlist_id, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=71
        """
        url = 'https://openapi.youku.com/v2/playlists/videos.json'
        params = {
            'client_id': self.client_id,
            'playlist_id': playlist_id,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def create_playlist(self, access_token, title, tags,
                        category=None, description=None):
        """doc: http://open.youku.com/docs/doc?id=72
        """
        url = 'https://openapi.youku.com/v2/playlists/create.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'title': title,
            'tags': tags,
            'category': category,
            'description': description
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def update_playlist(self, access_token, playlist_id, title,
                        tags=None, category=None, description=None):
        """doc: http://open.youku.com/docs/doc?id=73
        """
        url = 'https://openapi.youku.com/v2/playlists/update.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'playlist_id': playlist_id,
            'title': title,
            'tags': tags,
            'category': category,
            'description': description
        }
        data = remove_none_value(data)
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def destroy_playlist(self, access_token, playlist_id):
        """doc: http://open.youku.com/docs/doc?id=74
        """
        url = 'https://openapi.youku.com/v2/playlists/destroy.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'playlist_id': playlist_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def add_videos_to_playlist(self, access_token, playlist_id, video_ids):
        """doc: http://open.youku.com/docs/doc?id=75
        """
        url = 'https://openapi.youku.com/v2/playlists/video/add.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'playlist_id': playlist_id,
            'video_ids': video_ids
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def del_videos_from_playlist(self, access_token, playlist_id, video_ids):
        """doc: http://open.youku.com/docs/doc?id=76
        """
        url = 'https://openapi.youku.com/v2/playlists/video/del.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'playlist_id': playlist_id,
            'video_ids': video_ids
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def set_cover_video_for_playlist(self, access_token, playlist_id,
                                     video_id):
        """doc: http://open.youku.com/docs/doc?id=77
        """
        url = 'https://openapi.youku.com/v2/playlists/video/setcover.json'
        data = {
            'client_id': self.client_id,
            'access_token': access_token,
            'playlist_id': playlist_id,
            'video_id': video_id
        }
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()['id']

    def find_next_video_in_playlist(self, playlist_id, cur_video_id):
        """doc: http://open.youku.com/docs/doc?id=78
        """
        url = 'https://openapi.youku.com/v2/playlists/video/next.json'
        params = {
            'client_id': self.client_id,
            'playlist_id': playlist_id,
            'video_id': cur_video_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
