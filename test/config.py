# -*- coding: utf-8 -*-
import json

# data for test, please replace it to yours
CLIENT_ID = 'your client id'
CLIENT_SECRET = 'your client secret'
REDIRECT_URI = 'http://127.0.0.1:5000/youku/authorize'
ACCESS_TOKEN = 'your access token'
USER_ID = '419384312'
USER_NAME = u'\u97e9\u56fd\u607a'


def print_json(obj):
    print json.dumps(obj, indent=4, sort_keys=True)
