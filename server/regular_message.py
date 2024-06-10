from global_arrays import *
from message_manipulations import *


class Regular_Message():
    def __init__(self, data, client, key) -> None:
        self.data = data
        self.client = client
        self.key = key
        x = DICT_OF_ROOM_IN_GUY[self.client]
        user_list = DICT_OF_PEOPLE_IN_ROOM[x]
        for socket in user_list:
            if socket is not self.client:
                Message_Manipulations(
                    self.key, socket).sending_message(self.data)
