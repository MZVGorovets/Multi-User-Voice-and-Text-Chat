from global_arrays import *
from message_manipulations import *


class Join_Room():
    def __init__(self, room_name, room_password, client, key):
        self.room_name = room_name
        self.room_password = room_password
        self.client = client
        self.key = key

        if self.room_name in DICT_OF_ROOMS:
            if DICT_OF_ROOMS[self.room_name] == self.room_password:
                DICT_OF_ROOM_IN_GUY[self.client] = self.room_name
                DICT_OF_PEOPLE_IN_ROOM[self.room_name].append(self.client)
                Message_Manipulations(
                    self.key, self.client).sending_message("200")
            else:
                Message_Manipulations(
                    self.key, self.client).sending_message("400")
        else:
            Message_Manipulations(self.key, self.client).sending_message("400")
