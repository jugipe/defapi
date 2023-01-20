"""
Wolt Summer 2023 Engineering Internships
Preliminary Assignment for Engineering Positions
Backend

Creator: Jukka Pelli, jukka.pelli@tuni.fi

This Python program is a simple single point REST API which parses a http request
containing the data of an delivery order as payload and returns the calculated
delivery fee in the response payload
"""
from fastapi import FastAPI, HTTPException
from models.order import Order
from delivery_fee_calculator.delivery_fee_calculator import calculate_delivery_fee

app = FastAPI()

@app.post('/')
def post_calc_order(order: Order):
    """POST method of the API. Validates the payload and returns
    the calculated fee as response"""

    # Calculate the fee, catch calculator errors and return internal server error
    # if something goes wrong in the fee calculation
    try:
        delivery_fee:int = calculate_delivery_fee(order)
        return {"delivery_fee": delivery_fee}
    except:
        raise HTTPException(status_code=500)


