from global_arrays import *
from message_manipulations import *


class Exit_Room():
    def __init__(self, username, room_name, client, key):
        self.username = username
        self.room_name = room_name
        self.client = client
        self.key = key

        DICT_OF_PEOPLE_IN_ROOM[self.room_name].remove(self.client)
        del DICT_OF_ROOM_IN_GUY[self.client]
        Message_Manipulations(
            self.key, self.client).sending_message("exit!!!exit")
