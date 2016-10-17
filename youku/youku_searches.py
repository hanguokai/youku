"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from .util import check_error, remove_none_value


class YoukuSearchs(object):

    """Youku Searchs API.

    doc: http://open.youku.com/docs/api_searches.html
    """

    def __init__(self, client_id):
        super(YoukuSearchs, self).__init__()
        self.client_id = client_id

    def search_videos_by_tag(self, tag, category=None,
                             period='today',
                             orderby='relevance',
                             page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=80
        """
        url = 'https://openapi.youku.com/v2/searches/video/by_tag.json'
        params = {
            'client_id': self.client_id,
            'tag': tag,
            'period': period,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        if category:
            params['category'] = category
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_videos_by_keyword(self, keyword, category=None,
                                 period='week', orderby='relevance',
                                 public_type='all', paid=None,
                                 timeless=None, timemore=None,
                                 streamtypes=None,
                                 page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=81
        """
        url = 'https://openapi.youku.com/v2/searches/video/by_keyword.json'
        params = {
            'client_id': self.client_id,
            'keyword': keyword,
            'category': category,
            'period': period,
            'orderby': orderby,
            'public_type': public_type,
            'paid': paid,
            'timeless': timeless,
            'timemore': timemore,
            'streamtypes': streamtypes,
            'page': page,
            'count': count
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_shows_by_keyword(self, keyword, unite=0, source_site=None,
                                category=None, release_year=None,
                                area=None, orderby='view-count',
                                paid=None, hasvideotype=None,
                                page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=82
        """
        url = 'https://openapi.youku.com/v2/searches/show/by_keyword.json'
        params = {
            'client_id': self.client_id,
            'keyword': keyword,
            'unite': unite,
            'source_site': source_site,
            'category': category,
            'release_year': release_year,
            'area': area,
            'orderby': orderby,
            'paid': paid,
            'hasvideotype': hasvideotype,
            'page': page,
            'count': count
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_keyword_complete(self, keyword):
        """doc: http://open.youku.com/docs/doc?id=83
        """
        url = 'https://openapi.youku.com/v2/searches/keyword/complete.json'
        params = {
            'client_id': self.client_id,
            'keyword': keyword
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_keyword_top(self, category=None, count=20, period='today'):
        """doc: http://open.youku.com/docs/doc?id=84
        """
        url = 'https://openapi.youku.com/v2/searches/keyword/top.json'
        params = {
            'client_id': self.client_id,
            'count': count,
            'period': period
        }
        if category:
            params['category'] = category
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_show_address_unite(self, progammeId,
                                  source_site=None, type=None):
        """doc: http://open.youku.com/docs/doc?id=85
        """
        url = 'https://openapi.youku.com/v2/searches/show/address_unite.json'
        params = {
            'client_id': self.client_id,
            'progammeId': progammeId,
            'source_site': source_site,
            'type': type
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def search_show_top_unite(self, category, genre=None, area=None,
                              year=None, orderby=None, headnum=1,
                              tailnum=1, onesiteflag=None,
                              page=1, count=20):
        """doc: http://open.youku.com/docs/doc?id=86
        """
        url = 'https://openapi.youku.com/v2/searches/show/top_unite.json'
        params = {
            'client_id': self.client_id,
            'category': category,
            'genre': genre,
            'area': area,
            'year': year,
            'orderby': orderby,
            'headnum': headnum,
            'tailnum': tailnum,
            'onesiteflag': onesiteflag,
            'page': page,
            'count': count
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
