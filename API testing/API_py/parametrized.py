import requests
import pytest
from assertpy import assert_that
from lxml import etree


the_api_response = {
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}

URL = 'https://jsonplaceholder.typicode.com/'
URL_post = URL + 'post'
test_data_user = [
    (1, "Leanne Graham", ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']),
    # (!) it would be very helpful to use test_data and parametrize instead of a for loop,
    # because in case the first test will fail(1, "Leanne Graham") then the test with the next test data will not be
    # executed anymore
    # (2, "Ervin Howell"),
    # (3, "Clementine Bauch")
]


def some_func(arg):
    return 1/arg

# (!) it would be very helpful to use test_data and parametrize instead of a for loop, because in case the first
# test will fail(1, "Leanne Graham") then the test with the next test data will not be executed anymore
@pytest.mark.parametrize("userid, expected_name, list_keys", test_data_user)
def test_parametrize(userid, expected_name, list_keys):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    json_resp = dict(response.json())
    # assert response.status_code == 200
    # assert json_resp["id"] == userid
    # assert json_resp["name"] == expected_name
    assert_that(json_resp['id']).is_less_than(3)
    for key_value in list_keys:
        assert_that(json_resp).contains_key(key_value)
    assert_that(json_resp['name']).contains('L')  # This type of assertion verify if the value of the 'name' key contains L
    assert_that(json_resp).has_username('Bret')
    assert_that(some_func).raises(ZeroDivisionError).when_called_with(0)
