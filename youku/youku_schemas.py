"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from util import check_error


class YoukuSchemas(object):

    """Youku Schemas API.
    """

    def __init__(self, client_id):
        super(YoukuSchemas, self).__init__()
        self.client_id = client_id

    def video_category(self):
        """doc: http://open.youku.com/docs/doc?id=90
        """
        url = 'https://openapi.youku.com/v2/schemas/video/category.json'
        r = requests.get(url)
        check_error(r)
        return r.json()

    def upload_spec(self):
        """doc: http://open.youku.com/docs/doc?id=91
        """
        url = 'https://openapi.youku.com/v2/schemas/upload/spec.json'
        r = requests.get(url)
        check_error(r)
        return r.json()

    def comment_expression(self):
        """doc: http://open.youku.com/docs/doc?id=92
        """
        url = 'https://openapi.youku.com/v2/schemas/comment/expression.json'
        r = requests.get(url)
        check_error(r)
        return r.json()

    def show_category(self):
        """doc: http://open.youku.com/docs/doc?id=93
        """
        url = 'https://openapi.youku.com/v2/schemas/show/category.json'
        r = requests.get(url)
        check_error(r)
        return r.json()

    def playlist_category(self):
        """doc: http://open.youku.com/docs/doc?id=94
        """
        url = 'https://openapi.youku.com/v2/schemas/playlist/category.json'
        r = requests.get(url)
        check_error(r)
        return r.json()

    def searche_top_category(self):
        """doc: http://open.youku.com/docs/doc?id=95
        """
        url = 'https://openapi.youku.com/v2/schemas/searche/top/category.json'
        r = requests.get(url)
        check_error(r)
        return r.json()
