import requests
import json
import logging as logger
from src.helpers.confighelper import ConfigHelper
from src.helpers.datahelpers import DataHelpers
from src.manager.requestmanager import RequestManager
from genson import SchemaBuilder
import re


class ApiManager(object):

    def __init__(self):
        # get_token = TokenManager()
        config_obj = ConfigHelper()
        self.baseurl = config_obj.get_base_url()

    def post_request_200ok(self, end_point, req_body_folder, additional_args=None):
        request_manager = RequestManager()
        url = self.baseurl + end_point
        response = request_manager.post_request(url, req_body_folder)
        return response.status_code

    def get_request_200ok(self, end_point, req_body_folder, additional_args=None):
        request_manager = RequestManager()
        url = self.baseurl + end_point
        if req_body_folder is not None:
            response = request_manager.get_request_with_body_request(url, req_body_folder)
        else:
            response = request_manager.get_request_without_body_request(url)
        return response.status_code

    def post_request_compare_schema(self, end_point, req_body_folder, res_body_path, additional_args=None, true=None):
        request_manager = RequestManager()
        url = self.baseurl + end_point
        expacted_schema = get_schema_from_payload(res_body_path)

        response = request_manager.post_request(url, req_body_folder)
        builder = SchemaBuilder()
        builder.add_object(response.json())
        payload_schema = builder.to_schema()
        if expacted_schema == payload_schema:
            return True
        else:
            return False

    def post_request_compare_schema_keys(self, end_point, req_body_folder, res_body_path,
                                                    additional_args=None, true=None):
        request_manager = RequestManager()
        url = self.baseurl + end_point
        expected_schema = get_schema_from_payload(res_body_path)

        response = request_manager.post_request(url, req_body_folder)
        builder = SchemaBuilder()
        builder.add_object(response.json())
        payload_schema = builder.to_schema()
        expected_keys = get_all_keys(expected_schema)
        api_keys = get_all_keys(payload_schema)
        check = all(item in expected_keys for item in api_keys)
        return check


def get_schema_from_payload(res_body_path):
    request_manager = RequestManager()
    expected_res = request_manager.get_expacted_payload(res_body_path)
    builder = SchemaBuilder()
    builder.add_object(expected_res)
    payload_schema = builder.to_schema()
    return payload_schema


def get_all_keys(payload_schema):
    schema_string = json.dumps(payload_schema)
    str_lens = len(schema_string)
    filter_d = [m.start() for m in re.finditer('required', schema_string)]
    print(filter_d)
    all_keys = []
    for item in filter_d:
        substring = schema_string[item + 11:str_lens]
        end_string = substring.index(']')
        sub_element = substring[0:end_string + 1]
        ele_list = json.loads(sub_element)
        all_keys = list(set(all_keys + ele_list))
    return all_keys
