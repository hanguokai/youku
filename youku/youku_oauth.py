"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""
import requests
try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    from urllib import urlencode
from util import check_error


class YoukuOauth(object):

    """Youku Oauth API.

    doc: http://open.youku.com/docs/doc?id=100
    """

    def __init__(self, client_id, client_secret, redirect_uri):
        super(YoukuOauth, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize_url(self, state=''):
        """ return user authorize url
        """
        url = 'https://openapi.youku.com/v2/oauth2/authorize?'
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'state': state,
            'redirect_uri': self.redirect_uri
        }
        return url + urlencode(params)

    def get_token_by_code(self, code):
        '''return origin json'''
        url = 'https://openapi.youku.com/v2/oauth2/token'
        data = {'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.redirect_uri}
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def get_token_by_password(self, username, password):
        ''' To use this method, you must be cooperation level with youku.
        return origin json
        '''
        url = 'https://openapi.youku.com/v2/oauth2/token'
        data = {'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'password',
                'username': username,
                'password': password}
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()

    def refresh_token(self, refresh_token):
        '''return origin json'''
        url = 'https://openapi.youku.com/v2/oauth2/token'
        data = {'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token}
        r = requests.post(url, data=data)
        check_error(r)
        return r.json()
