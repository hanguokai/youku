"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from .util import check_error, remove_none_value


class YoukuShows(object):

    """Youku Shows API.

    doc: http://open.youku.com/docs/api_shows.html
    """

    def __init__(self, client_id):
        super(YoukuShows, self).__init__()
        self.client_id = client_id

    def find_show_by_id(self, show_id):
        """doc: http://open.youku.com/docs/doc?id=59
        """
        url = 'https://openapi.youku.com/v2/shows/show.json'
        params = {
            'client_id': self.client_id,
            'show_id': show_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_shows_by_ids(self, show_ids):
        """doc: http://open.youku.com/docs/doc?id=60
        """
        url = 'https://openapi.youku.com/v2/shows/show_batch.json'
        params = {
            'client_id': self.client_id,
            'show_ids': show_ids
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_show_premium_by_ids(self, show_ids, page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=61
        """
        url = 'https://openapi.youku.com/v2/shows/show_premium.json'
        params = {
            'client_id': self.client_id,
            'show_ids': show_ids,
            'page': page,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_shows_by_category(self, category, genre=None, area=None,
                               release_year=None, paid=None,
                               orderby='view-today-count',
                               streamtypes=None, person=None,
                               page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=62
        """
        url = 'https://openapi.youku.com/v2/shows/by_category.json'
        params = {
            'client_id': self.client_id,
            'category': category,
            'genre': genre,
            'area': area,
            'release_year': release_year,
            'paid': paid,
            'orderby': orderby,
            'streamtypes': streamtypes,
            'person': person,
            'page': page,
            'count': count
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_shows_by_related(self, show_id,
                              count=20):
        """doc: http://open.youku.com/docs/doc?id=63
        """
        url = 'https://openapi.youku.com/v2/shows/by_related.json'
        params = {
            'client_id': self.client_id,
            'show_id': show_id,
            'count': count
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_videos_by_show(self, show_id, show_videotype=None,
                            show_videostage=None, orderby='videoseq-asc',
                            page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=64
        """
        url = 'https://openapi.youku.com/v2/shows/videos.json'
        params = {
            'client_id': self.client_id,
            'show_id': show_id,
            'page': page,
            'count': count,
            'show_videotype': show_videotype,
            'show_videostage': show_videostage,
            'orderby': orderby
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
