import requests
import json
import logging as logger
from src.helpers.confighelper import ConfigHelper
from src.helpers.datahelpers import DataHelpers


class RequestManager(object):

    def __init__(self):
        pass
        # config_obj = ConfigHelper()
        # self.baseurl = config_obj.get_base_url()

    def post_request(self, url, req_body_folder, additional_args=None):
        datahelper = DataHelpers()
        payload_json = datahelper.getRequestBodyPayload(req_body_folder)
        headers = datahelper.getHeader()
        # url = self.baseurl + end_point
        response = requests.request("POST", url, headers=headers, data=payload_json)
        return response

    def get_request_with_body_request(self, url, req_body_folder, additional_args=None):
        datahelper = DataHelpers()
        payload_json = datahelper.getRequestBodyPayload(req_body_folder)
        headers = datahelper.getHeader()
        # url = self.baseurl + end_point
        response = requests.request("GET", url, headers=headers, data=payload_json)
        return response

    def get_request_without_body_request(self, url, additional_args=None):
        datahelper = DataHelpers()
        headers = datahelper.getHeader()
        response = requests.request("GET", url, headers=headers)
        return response

    def get_expacted_payload(self, expacted_response):
        datahelper = DataHelpers()
        payload_json = datahelper.getResponseBodyPayload(expacted_response)
        return payload_json

