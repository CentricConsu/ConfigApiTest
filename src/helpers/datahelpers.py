import json
import logging as logger
import os

from src.helpers.confighelper import ConfigHelper


class DataHelpers(object):

    def __init__(self):
        config_obj = ConfigHelper()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        api_token = config_obj.get_access_token()
        self.access_token = api_token

    def getRequestBodyPayload(self, request_body_path, additional_args=None):
        json_body = request_body_path.split('/')
        if len(json_body) != 2:
            logger.error('Wrong request body path for request body ' + request_body_path)
        else:
            template_payload = os.path.join(self.cur_file_dir, '..', 'data', 'request_body', json_body[0], json_body[1])
            with open(template_payload) as f:
                payload = json.load(f)
                return json.dumps(payload)

    def getResponseBodyPayload(self, request_body_path, additional_args=None):
        json_body = request_body_path.split('/')
        if len(json_body) != 2:
            logger.error('Wrong request body path for request body ' + request_body_path)
        else:
            template_payload = os.path.join(self.cur_file_dir, '..', 'data', 'response_body', json_body[0],
                                            json_body[1])
            with open(template_payload) as f:
                payload = json.load(f)
                return payload

    def getHeader(self, additional_args=None):
        raw_headers = os.path.join(self.cur_file_dir, '..', 'data', 'headers', 'headers.json')
        with open(raw_headers) as f:
            header_json = json.load(f)
            bearer_token = {'Authorization': 'Bearer ' + self.access_token}
            header_json.update(bearer_token)
            return header_json
