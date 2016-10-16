try:
    # Python 3
    from urllib.parse import parse_qs
except ImportError:
    # Python 2
    from urlparse import parse_qs


def check_error(response, expect_status=200):
    """
    Youku error should return in json form, like:
    HTTP 400
    {
        "error":{
            "code":120010223,
            "type":"UploadsException",
            "description":"Expired upload token"
        }
    }

    But error also maybe in response url params or response booy.

    Content-Type maybe application/json or text/plain, so
    don't relay on it.

    Args:
        expect_status: normally is 200 or 201
    """
    json = None
    try:
        json = response.json()
    except:
        pass
    if (response.status_code != expect_status or
            response.status_code == 400 or
            'error' in json):
        if json:
            error = json['error']
            raise YoukuError(error['code'], error['type'],
                             error['description'], response.status_code)
        else:
            # try to parse error from body
            error = parse_qs(response.text)
            raise YoukuError(error.get('code', [None])[0],
                             error.get('type', [None])[0],
                             error.get('description', [None])[0],
                             response.status_code)


def remove_none_value(data):
    """remove item from dict if value is None.
    return new dict.
    """
    return dict((k, v) for k, v in data.items() if v is not None)


class YoukuError(Exception):

    """ Youku error.
        It has three attributes: code, type, description.
        http://open.youku.com/docs/upload_client_chinese.html#error-definition
    """

    def __init__(self, code, _type, description, status_code):
        self.code = code
        self.type = _type
        self.description = description
        self.status_code = status_code

    def __str__(self):
        return ("http_status: %s, error: %s, %s, %s" %
                (self.status_code, self.code, self.type, self.description))
