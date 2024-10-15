import allure
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.contants.api_constants import APIConstants
from src.helpers.Payload_manager  import *
from src.helpers.Common_verification import *
from src.utils.utils import utils
import scope

@pytest.fixture((scope=="session")
    def create_token():
    response=post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=utils().common_header_json(),
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture((scope=="session")
    def get_booking_id():
    response=post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=utils().common_header_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id=response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return booking_id