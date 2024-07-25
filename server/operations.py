from cryptography.fernet import Fernet
from message_manipulations import *
from supersocket import *
from database import *
from global_arrays import *
from sign_in import *
from sign_up import *
from create_room import *
from join_room import *
from exit_room import *
from receiving_sound import *
from regular_message import *
from message_manipulations import *
from supersocket import *


class Operations:
    # getting a message and understanding what they doing
    def __init__(self, client, key, db):
        self.db = db
        self.client = client
        self.key = key
        self.public_key = SuperSocket(self.client).recv_msg()
        ciphered_key = Key_Encryption(self.key, self.public_key).returning()
        SuperSocket(self.client).send_msg(ciphered_key)

        while True:
            self.data = Message_Manipulations(
                self.key, self.client).receiving_message()
            splited_data = self.data.split("!!!")

            if splited_data[0] == "sign_in":
                Sign_In(splited_data[1], self.client, self.key, self.db)


# ___________________________________________________________________________________________________________________________________
            elif splited_data[0] == "sign_up":
                Sign_Up(splited_data[1], self.client, self.key, self.db)


# ___________________________________________________________________________________________________________________________________
            elif splited_data[0] == "create_room":
                Create_Room(splited_data[1],
                            splited_data[2], self.client, self.key)

# ___________________________________________________________________________________________________________________________________
            elif splited_data[0] == "join_room":
                Join_Room(splited_data[1],
                          splited_data[2], self.client, self.key)

            elif splited_data[0] == "exit":
                Exit_Room(splited_data[1],
                          splited_data[2], self.client, self.key)

            elif splited_data[0] == "sound":
                Receiving_Sound(self.data, self.client, self.key)

            else:
                Regular_Message(self.data, self.client, self.key)
