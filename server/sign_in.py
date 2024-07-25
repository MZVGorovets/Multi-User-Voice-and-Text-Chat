from database import *
from message_manipulations import *


class Sign_In():
    def __init__(self, info, client, key, db):
        self.db = db
        self.info = info
        self.client = client
        self.key = key
        password = Message_Manipulations(
            self.key, self.client).receiving_message()
        if (self.db.username_exists(self.info) and self.db.check_password(self.info, password)):
            Message_Manipulations(self.key, self.client).sending_message("200")

        else:
            Message_Manipulations(self.key, self.client).sending_message("400")
