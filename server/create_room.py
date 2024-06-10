from global_arrays import *
from message_manipulations import *


class Create_Room():
    def __init__(self, room_name, room_password, client, key):
        self.room_name = room_name
        self.room_password = room_password
        self.client = client
        self.key = key

        if self.room_name in DICT_OF_ROOMS:
            Message_Manipulations(self.key, self.client).sending_message("400")
        else:
            Message_Manipulations(self.key, self.client).sending_message("200")
            DICT_OF_ROOMS[self.room_name] = self.room_password
            DICT_OF_PEOPLE_IN_ROOM[self.room_name] = []
