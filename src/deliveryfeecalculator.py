"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This module defines the functions needed for calculating delivery fees based on
the cart value, the delivery distance, the number of items in the cart and the time of the order

Calculator uses a config.json file to determine the rules of calculating the delivery fee
"""
import json
from pydantic import ValidationError
from datetime import datetime
from models import *


# Parse the config.json to Calc_config and validate it at the same time
with open("config.json") as conf:
    try:
        calculator_rules = Calc_config.parse_obj(json.load(conf))
    except ValidationError as err:
        print(err)

def calculate_delivery_fee(order: Order) -> int:
    """Function for calculating the total delivery fee"""

    # initial delivery fee
    delivery_fee = 0

    # No need to calculate further if the order value is above large order
    # Because they are free of delivery charge
    if(order.cart_value >= calculator_rules.large_order):
        return delivery_fee

    # Add the surcharges based on order value and number of items in the order
    cart_fee = calculate_cart_fee(order.cart_value, order.number_of_items)

    # Add the delivery charge based on distance
    distance_fee = calculate_distance_fee(order.delivery_distance)

    # Sum the cart and distance fee to the delivery fee
    delivery_fee = cart_fee + distance_fee

    # Multiply the fee if it is friday rush multiplier and round
    # to the nearest whole number
    if (is_friday_rush(order.time)):
        delivery_fee = round(delivery_fee * calculator_rules.friday_rush_multiplier)

    # Check that the delivery fee doesn't exceed max delivery fee, it does return the
    # max delivery fee instead
    if delivery_fee > calculator_rules.max_delivery_fee:
        delivery_fee = calculator_rules.max_delivery_fee

    return delivery_fee

def calculate_cart_fee(cart_value: int, number_of_items: int) -> int:
    """Function for calculating the total surcharges based on cart value and number 
    of ordered items
    """
    # initial cart fee
    cart_fee = 0

    # Add a surcharge if the total order is less than the small order limit        
    if cart_value < calculator_rules.small_order:
        cart_fee += calculator_rules.small_order - cart_value

    # Add a surcharge for every item in the cart after it exceeds the limit defined
    if number_of_items > calculator_rules.nro_of_cart_items_without_fee:
        cart_fee += calculator_rules.extra_cart_items_fee * (number_of_items - calculator_rules.nro_of_cart_items_without_fee)

    # Add the bulk fee if needed
    if number_of_items > calculator_rules.bulk_limit:
        cart_fee += calculator_rules.bulk_fee

    return cart_fee

def calculate_distance_fee(delivery_distance: int) -> int:
    """Function counts the addition totalal fee based on distance the courier
    needs to travel"""
        
    # Add the default distance fee, which covers a default distance of courier travel
    # if distance is below default distance no need to calculate more
    distance_fee = calculator_rules.default_distance_fee
    if delivery_distance <= calculator_rules.default_distance_meters:
        return distance_fee

    # For every extra meter from default distance add the extra distance fee to the distance fee
    extra_distance_fee = recursive_distance_fee_calc(delivery_distance - calculator_rules.default_distance_meters)
    distance_fee += extra_distance_fee

    return distance_fee

def recursive_distance_fee_calc(distance: int) -> int:
    """Function for counting the ad totalditional distance fee."""

    if distance <= calculator_rules.extra_distance_meters:
        return calculator_rules.extra_distance_fee
    else:
        return calculator_rules.extra_distance_fee + recursive_distance_fee_calc(distance - calculator_rules.extra_distance_meters)

def is_friday_rush(time: datetime) -> bool:
    """Function for checking if the total order time is during the Friday rush
    which is every friday between 3 - 7 PM
    """

    # No need to continue if its not friday
    if (time.weekday() != 4):
        return False

    # No need to continue if its not between 3PM and 7PM
    if (time.hour not in range(15, 19)):
        return False

    # If we end up here, it must be friday between 3PM - 7PM
    return True




    
