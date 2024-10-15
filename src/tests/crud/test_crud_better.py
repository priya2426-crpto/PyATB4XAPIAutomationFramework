import pytest
import allure
from src.helpers.api_requests_wrapper import post_request
from src.contants.api_constants import APIConstants
from src.helpers.Payload_manager  import *
from src.helpers.Common_verification import *
from src.utils.utils import utils
class TestCRUDbooking(object):

    @pytest.mark.put
    @allure.title("test CRUD operation update(put).")
    @allure.description("verify that full update of booking id and Token is working")
def test_delete_bookingid_token(self, create_token, get_booking_id):
        put_url = APIConstants().url_patch_put_delete(booking_id=get_booking_id)
        print(put_url)
        response = delete_requests(
            url=delete_url,
            headers=utils().common_hedaer_put_delete_patch_cookie(token=create_token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response,expected_data=201)

        verify_respinse_key()(response.json()["firstname"], "Amit")
        verify_respinse_key()(response.json()["lastname"], "brown")
        verify_http_status_code(response_data=response, expected_data=200)

