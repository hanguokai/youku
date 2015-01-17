"""Youku Open API V2 Python Client

doc: http://open.youku.com/docs/tech_doc.html
"""

import requests
from util import check_error, remove_none_value


class YoukuPersons(object):

    """Youku Persons API.
    """

    def __init__(self, client_id):
        super(YoukuPersons, self).__init__()
        self.client_id = client_id

    def find_person_by_id(self, person_id):
        """doc: http://open.youku.com/docs/docs?id=87
        """
        url = 'https://openapi.youku.com/v2/persons/show.json'
        params = {
            'client_id': self.client_id,
            'person_id': person_id
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_persons_by_ids(self, person_ids):
        """doc: http://open.youku.com/docs/docs?id=88
        """
        url = 'https://openapi.youku.com/v2/persons/show_batch.json'
        params = {
            'client_id': self.client_id,
            'person_ids': person_ids
        }
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()

    def find_persons_by_type(self, type, nationality=None, gender=None,
                             firstletter=None, orderby='view-week-count',
                             page=1, count=20):
        """doc: http://open.youku.com/docs/docs?id=89
        """
        url = 'https://openapi.youku.com/v2/persons/by_type.json'
        params = {
            'client_id': self.client_id,
            'type': type,
            'nationality': nationality,
            'gender': gender,
            'firstletter': firstletter,
            'orderby': orderby,
            'page': page,
            'count': count
        }
        params = remove_none_value(params)
        r = requests.get(url, params=params)
        check_error(r)
        return r.json()
