"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This module defines the model of an Order to against
we can validate
"""
from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime