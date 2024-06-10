from message_manipulations import *


class Room_Manipulations():
    def __init__(self, room_name, room_password, client_socket, key, username):
        self.room_name = room_name
        self.room_password = room_password
        self.client_socket = client_socket
        self.key = key
        self.username = username

    def create_room(self):
        Message_Manipulations(self.key, self.client_socket).sending_message(
            "create_room" + "!!!" + self.room_name+"!!!"+self.room_password)
        if int(Message_Manipulations(self.key, self.client_socket).receiving_message()) == 200:
            return True
        else:
            return False

    def join_room(self):
        Message_Manipulations(self.key, self.client_socket).sending_message(
            "join_room" + "!!!" + self.room_name + "!!!" + self.room_password + "!!!" + self.username)
        if int(Message_Manipulations(self.key, self.client_socket).receiving_message()) == 200:
            return True
        else:
            return False
