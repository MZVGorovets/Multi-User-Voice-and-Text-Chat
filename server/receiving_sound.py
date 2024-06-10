import time
from global_arrays import *
from message_manipulations import *


class Receiving_Sound():
    def __init__(self, data, client, key) -> None:
        self.data = data
        self.client = client
        self.key = key
        main_data = Message_Manipulations(
            self.key, self.client).receiving_audio()
        x = DICT_OF_ROOM_IN_GUY[self.client]
        user_list = DICT_OF_PEOPLE_IN_ROOM[x]
        for socket in user_list:
            Message_Manipulations(
                self.key, socket).sending_message(self.data)
            time.sleep(3)
            Message_Manipulations(
                self.key, socket).sending_audio(main_data)
