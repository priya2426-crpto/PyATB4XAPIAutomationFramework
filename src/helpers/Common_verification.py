#Common_verification
#HTTP STATUS CODE
#HEDAERS
#DATA VERIFICATION
#JSON SCHEMA
def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code==expected_data,"failed status code match"

def verify_respinse_key(key,expected_data):
    assert key==expected_data

def verify_json_key_for_not_null(key):
    assert key!=0,"failed - key is non empty"+key
    assert key > 0, "failed - key is greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key!=0,"failed - key is non empty"+key
