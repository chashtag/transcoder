import json

from . import urlencoded, xml

class Transcoder(object):
    def __init__(self,  req):
        self.req = req


    def get_type(self,) -> str:
        if self.req.content_type:
            return self.req.content_type
        return None


    def transcode_from_type(self, content_type) -> dict:
        match content_type:
            case 'application/x-www-form-urlencoded':
                return urlencoded.parse(self.req.get_data())
            case 'application/xml':
                return xml.parse(self.req.get_data())
            case 'application/json':
                return json.loads(self.req.get_data())
            case None:
                return {}
            case _:
                print(f'Content Type: {content_type}, not supported')
                return {}


    def get_dict(self,) -> dict:
        t = self.get_type()
        return self.transcode_from_type(t)
