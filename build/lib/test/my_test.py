import none as none
import requests
import json

from behave.formatter import null
from genson import SchemaBuilder
from pytest_schema import schema

payload2 = {
    "clientId": "D1E82E7157E1DD56EA158DB3E4A0013",
    "clientSecret": None
}
article_v1 = {
    "clientId": str,
    "clientSecret": str
}
builder = SchemaBuilder()
builder1 = SchemaBuilder()
builder.add_object(payload2)
payload_schema = builder.to_schema()
url = "http://proteus.cmiprog.com/AuthorizationManagement/api/v1/Register/ClientCredential"

payload = json.dumps({
    "applicationName": "test",
    "redirectUrl": "",
    "requestedScopes": [
        "backend"
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'NSC_ESNS=26fe32be-b0d8-1220-9678-005056861936_3578618070_2106411978_00000000000653209034'
}


def test_create_first_test_case():
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200


def test_create_second_test_case():
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 401


def test_create_third_test_case():
    response = requests.request("POST", url, headers=headers, data=payload)
    builder.add_object(response.json())
    payload_schema1 = builder.to_schema()
    assert payload_schema == payload_schema1
