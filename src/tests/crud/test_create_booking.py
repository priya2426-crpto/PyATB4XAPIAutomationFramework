#API testcase
#URL-->API Constants
#Headers-->utils.py
#payload-->payload_,anger.py
#HTTP Post-->api_request_wrapper.py
#verification-->common_verification.py

import allure
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.contants.api_constants import APIConstants
from src.helpers.Payload_manager  import payload_create_booking
from src.helpers.Common_verification import *
from src.utils.utils import utils
import logging

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify that create booking and booking id should not be null")
    @allure.description(
        "Creating a booking from the payload and verify that booking id shoud not be null")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("starting the testcase--TC1-positive")

        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=utils().common_header_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        LOGGER.info(response.json())["bookingid"]
        LOGGER.info("end of the testcase TC1-positive")

    @pytest.mark.negative
    @allure.title("verify that create booking and booking id should no payload")
    @allure.description(
        "Creating a booking from the payload and verify that booking id ")
    def test_create_booking_negative(self):
        LOGGER = logging.getLogger(__name__)


        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=utils().common_header_json(),
            payload={ },
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=500)