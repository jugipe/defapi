"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This module defines the model of delivery fee calculator settings to against
we can validate
"""
from pydantic import BaseSettings


class DeliveryFeeCalculatorSettings(BaseSettings):
    small_order: int
    large_order: int
    max_delivery_fee: int     
    default_distance_fee: int
    default_distance_meters: int
    extra_distance_fee: int
    extra_distance_meters: int
    nro_of_cart_items_without_fee: int 
    extra_cart_items_fee: int
    friday_rush_multiplier: float
    bulk_limit: int
    bulk_fee: int