import pytest
import requests
import json
import logging as logger
from src.manager.tokenmanager import get_access_token
from src.manager.apimanager import ApiManager

get_access_token(None)

test_data_zip_codes = [
    ("CodeLists/Search", "consumer_routes/post_codelist_search_req.json")
]


@pytest.mark.parametrize("endpoint,path", test_data_zip_codes)
def test_post_code_list_search_200ok(endpoint, path):
    api_manager = ApiManager()
    status_code = api_manager.post_request_200ok(endpoint, path)
    assert status_code == 200


def test_post_code_list_deployment_search_200ok():
    api_manager = ApiManager()
    status_code = api_manager.post_request_200ok("CodeLists/Deployments/Search",
                                                 "consumer_routes/post_code_list_deployment_search_req.json")
    assert status_code == 200


def test_post_code_list_deployment_search_compare_schema():
    api_manager = ApiManager()
    bool_res = api_manager.post_request_compare_schema("CodeLists/Deployments/Search",
                                                       "consumer_routes/post_code_list_deployment_search_req.json",
                                                       "consumer_routes/post_code_list_deployment_search_res.json")
    assert bool_res is True


def test_post_code_list_deployment_search_compare_keys():
    api_manager = ApiManager()
    bool_res = api_manager.post_request_compare_schema_keys("CodeLists/Deployments/Search",
                                                            "consumer_routes/post_code_list_deployment_search_req.json",
                                                            "consumer_routes/post_code_list_deployment_search_res.json")
    assert bool_res is True


def test_post_rate_factor_deployment_search_200ok():
    api_manager = ApiManager()
    status_code = api_manager.post_request_200ok("RateFactors/Deployments/Search",
                                                 "consumer_routes/post_rate_factor_deployment_search_req.json")
    assert status_code == 200


def test_get_impacted_code_list_200ok():
    api_manager = ApiManager()
    status_code = api_manager.get_request_200ok("CodeLists/1145/getImpactedCodeList?deploymentId=6472506", None)
    assert status_code == 200


def test_get_impacted_code_list_201ok():
    api_manager = ApiManager()
    status_code = api_manager.get_request_200ok("CodeLists/1145/getImpactedCodeList?deploymentId=6472506", None)
    assert status_code == 200
