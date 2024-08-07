from database import *
from message_manipulations import *


class Sign_Up():
    def __init__(self, info, client, key, db):
        self.db = db
        self.info = info
        self.client = client
        self.key = key
        password = Message_Manipulations(
            self.key, self.client).receiving_message()
        if self.db.username_exists(self.info):
            Message_Manipulations(self.key, self.client).sending_message("400")
        else:
            self.db.insert(self.info, password)
            Message_Manipulations(self.key, self.client).sending_message("200")
