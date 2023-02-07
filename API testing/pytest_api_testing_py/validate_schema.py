import pytest
import requests
from assertpy import assert_that
from cerberus import Validator

url = "https://jsonplaceholder.typicode.com/posts/1"
schema_to_check = {
    "userId": {'type': 'number', "allowed": [1,2,3]},
    "id": {'type': 'number'},
    "title": {'type': 'string'},
    "body": {'type': 'string'}
}


def test_validate_schema():
    response = requests.get(url)
    json_resp = response.json()
    validator = Validator(schema_to_check, require_all = True)
    valid_bool = validator.validate(json_resp)
    assert_that(valid_bool).is_true()
