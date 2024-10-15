#contain common utilities
#setting headers
#read data from excel file
#read data from csv,json file
#set the headers-application/json,application/xml

class utils(object):
    def common_headers_json(self):
        headers={
            "Content-Type": "application/json"
        }
        return headers
    def common_headers_put_patch_delete_basic_auth(self,basic_auth_value):
        headers={
            "Content-Type": "application/json"
            "Authorization" "Basic"+str(basic_auth_value)
        }
        return headers
    def common_hedaer_put_delete_patch_cookie(self,token):
        headers={
            "Content-Type": "application/json"
            "cookie" "token"+str(token)
        }
    def read_csv_file(self):
        pass
    def read_env_file(self):
        pass
    def read_database(self):
        pass
