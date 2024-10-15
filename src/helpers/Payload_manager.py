#payload
def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "breakfast"

    }
    return payload
def payload_create_token():
    payload={
            "username": "admin",
            "password": "password123"
    }
    return payload