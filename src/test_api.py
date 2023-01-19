"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This module contains the tests for the API
"""
from fastapi.testclient import TestClient
from api import app

test_client = TestClient(app)

def test_api_methods():
    """Function tests the allowed methods"""

    # Testing payload
    test_payload = {"cart_value":790, "delivery_distance":2235, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}

    # Store test values to a list and iterate through it
    # first element is the method, second the method to test, third the expected response and fourth the expected response
    test_list = [
        ("GET", test_client.get("/"), 405, {"detail": "Method Not Allowed"}),
        ("POST", test_client.post("/", json=test_payload), 200, {"delivery_fee": 710}),
        ("PUT", test_client.put("/", json=test_payload), 405, {"detail": "Method Not Allowed"}),
        ("DELETE", test_client.delete("/"), 405, {"detail": "Method Not Allowed"})
    ]

    for test in test_list:
        print("Testing", test[0], "method")
        response = test[1]
        assert response.status_code == test[2]
        assert response.json() == test[3]


def test_request_payload_validation():
    """Function tests the basic responses of the REST API with different request payloads"""
    # Store test values to a list of tuples and iterate through it
    # first element of each tuple is the api call and the second is the basic response expected
    test_list = [
        ({"cart_value":790, "delivery_distance":2235, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 200),
        ({"cart_value":"test", "delivery_distance":2235, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 422),
        ({"cart_value":1500, "delivery_distance":"test", "number_of_items":4, "time":"2021-10-12T13:00:00Z"},  422),
        ({"cart_value":1000, "delivery_distance":2235, "number_of_items":"k", "time":"2021-10-12T13:00:00Z"}, 422),
        ({"delivery_distance":5000, "number_of_items":20, "time":"2021-10-12T13:00:00Z"}, 422),
        ({"cart_value":500, "number_of_items":20, "time":"2021-10-12T13:00:00Z"}, 422),
        ({"cart_value":500, "delivery_distance":5000, "time":"2021-10-12T13:00:00Z"}, 422),
        ({"cart_value":500, "delivery_distance":5000, "number_of_items":20}, 422)
        ]

    for test in test_list:
        response = test_client.post("/", json=test[0])
        assert response.status_code == test[1]


def test_response_is_json():
    """Function tests that the return payload is json"""
    response = test_client.post("/", json={"cart_value":1000, "delivery_distance":2235, "number_of_items":6, "time":"2021-10-12T13:00:00Z"})
    assert response.json()
    assert response.headers.get("content-type") == "application/json"


def test_response_value_is_correct():
    # Store test values to a list of tuples and iterate through it
    # first element of each tuple is the api call and the second is the expected delivery fee value
    test_list = [
        ({"cart_value":790, "delivery_distance":2235, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 710),
        ({"cart_value":790, "delivery_distance":2235, "number_of_items":4, "time":"2023-01-13T15:05:00Z"}, 852),
        ({"cart_value":1000, "delivery_distance":1000, "number_of_items":4, "time":"2023-01-13T15:05:00Z"}, 240),
        ({"cart_value":15000, "delivery_distance":2235, "number_of_items":4, "time":"2021-10-12T13:00:00Z"},  0),
        ({"cart_value":1000, "delivery_distance":1000, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 200),
        ({"cart_value":1000, "delivery_distance":1000, "number_of_items":5, "time":"2021-10-12T13:00:00Z"}, 250),
        ({"cart_value":1000, "delivery_distance":1000, "number_of_items":10, "time":"2021-10-12T13:00:00Z"}, 500),
        ({"cart_value":1000, "delivery_distance":1000, "number_of_items":13, "time":"2021-10-12T13:00:00Z"}, 770),
        ({"cart_value":1000, "delivery_distance":1499, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 300),
        ({"cart_value":1000, "delivery_distance":1500, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 300),
        ({"cart_value":1000, "delivery_distance":1501, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 400),
        ({"cart_value":1000, "delivery_distance":5000, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 1000),
        ({"cart_value":1000, "delivery_distance":10000, "number_of_items":4, "time":"2021-10-12T13:00:00Z"}, 1500),
        ({"cart_value":50, "delivery_distance":10000, "number_of_items":50, "time":"2021-10-12T13:00:00Z"}, 1500)
        ]

    for test in test_list:
        response = test_client.post("/", json=test[0])
        assert response.json() ==  {"delivery_fee": test[1]}
