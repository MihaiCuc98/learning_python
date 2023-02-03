import requests
import pytest
from assertpy import assert_that

URL = 'https://jsonplaceholder.typicode.com/'
URL_post = URL + 'post'
test_data_user = [
    (1, "Leanne Graham"),  # (!) it would be very helpful to use test_data and parametrize instead of a for loop,
    # because in case the first test will fail(1, "Leanne Graham") then the test with the next test data will not be
    # executed anymore
    # (2, "Ervin Howell"),
    # (3, "Clementine Bauch")
]


# (!) it would be very helpful to use test_data and parametrize instead of a for loop, because in case the first
# test will fail(1, "Leanne Graham") then the test with the next test data will not be executed anymore
@pytest.mark.parametrize("userid, expected_name", test_data_user)
def test_parametrize(userid, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    json_resp = response.json()
    # assert response.status_code == 200
    # assert json_resp["id"] == userid
    # assert json_resp["name"] == expected_name
    assert_that(json_resp['id']).is_less_than(3)
    keys_value = list(json_resp.keys())
    print(keys_value)
    for key_value in keys_value:
        assert_that(json_resp).contains_key(key_value)
    assert_that(json_resp).extracting('name').contains('L')
