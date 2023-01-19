"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This module contains the unittests for the fee calculator, these
tests need updating if the calculating rules change
"""
from datetime import datetime
from models import Order
from deliveryfeecalculator import *


def test_calculate_fee():
    """Function tests that the delivery fee calculation returns correct delivery fee values
    with known values. 
    """

    # Store test values to a list of tuples and iterate through it
    # first element of each entry in the list is the needed values
    # to calculate the delivery fee and the second element is a known
    # delivery fee value for those parameters
    test_list = [({"cart_value": 790, "delivery_distance": 2235, 
                "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}, 710),
                ({"cart_value": 790, "delivery_distance": 2235, 
                "number_of_items": 4, "time": "2023-01-13T15:05:00Z"}, 852),
                ({"cart_value": 15000, "delivery_distance": 2235, 
                "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}, 0),
                ({"cart_value": 1000, "delivery_distance": 2235, 
                "number_of_items": 6, "time": "2021-10-12T13:00:00Z"}, 600),
                ({"cart_value": 500, "delivery_distance": 5000, 
                "number_of_items": 20, "time": "2021-10-12T13:00:00Z"}, 1500)]
        
    for entry in test_list:
        delivery_fee = calculate_delivery_fee(Order.parse_obj(entry[0]))
        assert delivery_fee == entry[1]

def test_test_calculate_cart_fee():
    """Function tests that the cart fee calculation returns correct fee values
    with known values. 
    """
    test_list = [
                ({"cart_value": 790, "number_of_items": 4}, 210),
                ({"cart_value": 790, "number_of_items": 6}, 310),
                ({"cart_value": 1000, "number_of_items": 6}, 100),
                ({"cart_value": 1000, "number_of_items": 13}, 570)
                ]

    for entry in test_list:
        cart_fee = calculate_cart_fee(entry[0]["cart_value"], entry[0]["number_of_items"])
        assert cart_fee == entry[1]

def test_calculate_distance_fee():
    """Function tests that the distance fee calculation returns correct fee values
    with known values. 
    """
    test_list = [
                (1000, 200),
                (1499, 300),
                (1500, 300),
                (1501, 400),
                (2235, 500)
                ]

    for entry in test_list:
        distance_fee = calculate_distance_fee(entry[0])
        assert distance_fee == entry[1]

def test_is_friday_rush():
    """Function tests that the friday rush checking returns correct values"""
    test_list = [
                (datetime(2023, 1, 13, 15, 5, 00), True),
                (datetime(2023, 1, 20, 18, 5, 00), True),
                (datetime(2023, 1, 13, 14, 59, 00), False),
                (datetime(2023, 1, 20, 19, 1, 00), False),
                (datetime(2023, 1, 19, 15, 5, 00), False)
                ]
    
    for entry in test_list:
        friday_rush = is_friday_rush(entry[0])
        assert friday_rush == entry[1]