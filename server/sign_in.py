from database import *
from message_manipulations import *


class Sign_In():
    def __init__(self, info, client, key):
        self.info = info
        self.client = client
        self.key = key
        password = Message_Manipulations(
            self.key, self.client).receiving_message()
        if (DB().username_exists(self.info) and DB().check_password(self.info, password)):
            Message_Manipulations(self.key, self.client).sending_message("200")

        else:
            Message_Manipulations(self.key, self.client).sending_message("400")
