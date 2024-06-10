import threading
import sounddevice as sd
import soundfile as sf
import pickle as pk
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import customtkinter
from authorization import *
from room_manipulations import *
from voice_recorder import *
from message_manipulations import *


class Sign_In_Window(customtkinter.CTk):
    def __init__(self, client_socket, key):
        self.key = key
        self.client_socket = client_socket

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_welcome = customtkinter.CTkLabel(master=self.frame_1, text="Welcome!", font=(
            "regular", 30))  # font name and size in px
        self.label_welcome.pack(pady=50, padx=10)

        self.username_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="username")
        self.username_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_log_in = customtkinter.CTkButton(
            master=self.frame_1, command=self.sign_in_func, text="log-in")
        self.button_log_in.pack(pady=10, padx=10)

        self.label_no_account = customtkinter.CTkLabel(master=self.frame_1, text="Don't have an account?", font=(
            "regular", 16))  # font name and size in px
        self.label_no_account.pack(pady=15, padx=10, ipadx=100)

        self.button_sign_up = customtkinter.CTkButton(
            master=self.frame_1, command=self.sign_up_window, text="sign-up")
        self.button_sign_up.pack(pady=10, padx=10)
        self.mainloop()

    def sign_in_func(self):
        self.username = str(self.username_textbox.get())
        self.password = str(self.password_textbox.get())
        if self.username == "":
            messagebox.showerror('Error', 'username not entered!')
        elif self.password == "":
            messagebox.showerror('Error', 'password not entered!')
        else:
            signed_in = Authorization(
                self.key, self.client_socket, self.username, self.password).sign_in()
            if signed_in:
                self.destroy()
                Main_Window(self.username, self.client_socket, self.key)
            else:
                messagebox.showerror('Error', 'password or username is wrong!')

    def sign_up_window(self):
        self.destroy()
        Sign_Up_Window(self.client_socket, self.key)


class Sign_Up_Window(customtkinter.CTk):
    def __init__(self, client_socket, key):
        self.key = key
        self.client_socket = client_socket

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_sign_up = customtkinter.CTkLabel(
            master=self.frame_1, text="Sign-Up", font=("regular", 30))  # font name and size in px
        self.label_sign_up.pack(pady=50, padx=10)

        self.username_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="username")
        self.username_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_sign_up = customtkinter.CTkButton(
            master=self.frame_1, command=self.sing_up_func, text="sign-up")
        self.button_sign_up.pack(pady=10, padx=10)

        self.button_back = customtkinter.CTkButton(
            master=self.frame_1, command=self.back, text="back")
        self.button_back.pack(pady=10, padx=10)

        self.mainloop()

    def sing_up_func(self):
        self.username = str(self.username_textbox.get())
        self.password = str(self.password_textbox.get())
        signed_up = Authorization(
            self.key, self.client_socket, self.username, self.password).sign_up()
        if signed_up:
            self.destroy()
            Sign_In_Window(self.client_socket, self.key)

        else:
            messagebox.showerror('Error', 'this username is exist!')

    def back(self):
        self.destroy()
        Sign_In_Window(self.client_socket, self.key)


class Main_Window(customtkinter.CTk):
    def __init__(self, username, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_happy_to_see = customtkinter.CTkLabel(
            master=self.frame_1, text="Happy to see you " + self.username + "!", font=("regular", 30))  # font name and size in px
        self.label_happy_to_see.pack(pady=50, padx=10)

        create_room = customtkinter.CTkButton(
            master=self.frame_1, text="create room", command=self.to_create_room_window)
        # Play button
        join_room = customtkinter.CTkButton(
            master=self.frame_1, text="join room", command=self.to_join_room_window)

        back_page = customtkinter.CTkButton(
            master=self.frame_1, text="back", command=self.back)

        create_room.pack(pady=10, padx=10)
        join_room.pack(pady=10, padx=10)
        back_page.pack(pady=10, padx=10)

        self.mainloop()

    def to_create_room_window(self):  # calling to create_room class
        self.destroy()
        Create_Room(self.username, self.client_socket, self.key)

    def to_join_room_window(self):  # calling to join_room class
        self.destroy()
        Join_Room(self.username, self.client_socket, self.key)

    def back(self):  # back to the sign-in window
        self.destroy()
        Sign_In_Window(self.client_socket, self.key)


class Create_Room(customtkinter.CTk):
    def __init__(self, username, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username
        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_create_room = customtkinter.CTkLabel(master=self.frame_1, text="create room", font=(
            "regular", 30))  # font name and size in px
        self.label_create_room.pack(pady=50, padx=10)

        self.room_name_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="room name")
        self.room_name_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_create_room = customtkinter.CTkButton(
            master=self.frame_1, command=self.creating_room, text="create room")
        self.button_create_room.pack(pady=10, padx=10)
        self.button_back = customtkinter.CTkButton(
            master=self.frame_1, command=self.back, text="back")
        self.button_back.pack(pady=10, padx=10)

        self.mainloop()

    def creating_room(self):
        self.room_name = str(self.room_name_textbox.get())
        self.room_password = str(self.password_textbox.get())
        created_room = Room_Manipulations(
            self.room_name, self.room_password, self.client_socket, self.key, self.username).create_room()
        if created_room:
            self.destroy()
            Main_Window(self.username, self.client_socket, self.key)
        else:
            messagebox.showerror('Error', 'this room is exist!')

    def back(self):  # back to the main window
        self.destroy()
        Main_Window(self.username, self.client_socket, self.key)


class Join_Room(customtkinter.CTk):
    def __init__(self, username, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username
        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_join_room = customtkinter.CTkLabel(master=self.frame_1, text="join room", font=(
            "regular", 30))  # font name and size in px
        self.label_join_room.pack(pady=50, padx=10)

        self.room_name_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="room name")
        self.room_name_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_join_room = customtkinter.CTkButton(
            master=self.frame_1, command=self.joining_room, text="join room")
        self.button_join_room.pack(pady=10, padx=10)
        self.button_back = customtkinter.CTkButton(
            master=self.frame_1, command=self.back, text="back")
        self.button_back.pack(pady=10, padx=10)

        self.mainloop()

    def joining_room(self):
        self.room_name = str(self.room_name_textbox.get())
        self.room_password = str(self.password_textbox.get())
        joined_room = Room_Manipulations(
            self.room_name, self.room_password, self.client_socket, self.key, self.username).join_room()
        if joined_room:
            self.destroy()
            Chat_Room(self.username, self.room_name,
                      self.client_socket, self.key).mainloop()
        else:
            messagebox.showerror('Error', 'this room is not exist!')

    def back(self):  # back to the main window
        self.destroy()
        Main_Window(self.username, self.client_socket, self.key)


class Chat_Room(customtkinter.CTk):
    def __init__(self, username, room_name, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username
        self.room_name = room_name
        self.num_of_files = 0

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.exit)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_hello_friend = customtkinter.CTkLabel(master=self.frame_left, text="Hello my friend", font=(
            "Roboto Medium", -16))  # font name and size in px
        self.label_hello_friend.pack(pady=10, padx=10)

        self.button_voice_msg = customtkinter.CTkButton(
            master=self.frame_left, text="Voice Message", command=self.voice_msg)
        self.button_voice_msg.pack(pady=10, padx=20)
        self.button_exit = customtkinter.CTkButton(
            master=self.frame_left, text="exit", command=self.exit)
        self.button_exit.pack(pady=10, padx=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============

        self.entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Enter message")
        self.entry.grid(row=8, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_send_msg = customtkinter.CTkButton(
            master=self.frame_right, text="Send message", border_width=2, fg_color=None,  command=self.send_message)
        self.button_send_msg.grid(
            row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.textbox = tk.Listbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=(
            220, 40), pady=(40, 80), sticky="nsew")

        self.target = threading.Thread(target=self.get_msg)
        self.target.start()

    # sending a message if this is not empty or tring to make trouble eith voice messages
    def send_message(self):
        self.message = self.entry.get()
        if "play audiofile trial" in self.message:
            messagebox.showerror(
                'Error', "you can't write something like this!")
        elif "" == self.message:
            messagebox.showerror(
                'Error', "you can't write something like this!")
        else:
            self.textbox.insert(END, self.username+": " + self.message)
            Message_Manipulations(self.key, self.client_socket).sending_message(
                "regular"+"!!!"+self.message+"!!!"+self.username)
            self.entry.delete(first_index=0, last_index=len(self.message))

    def voice_msg(self):  # calling to voice_recorder class
        Voice_Recorder_Window(self.username, self.client_socket, self.key)

    def exit(self):  # back to the main window
        Message_Manipulations(self.key, self.client_socket).sending_message(
            "exit" + "!!!"+self.username+"!!!"+self.room_name)
        self.destroy()
        Main_Window(self.username, self.client_socket, self.key)

    def get_msg(self):  # getting a voice or text messages and inserting them to the chat
        while True:
            try:
                the_message = Message_Manipulations(
                    self.key, self.client_socket).receiving_message()
                self.splited_message = the_message.split("!!!")

                if self.splited_message[0] == "sound":
                    the_main_data = (Message_Manipulations(
                        self.key, self.client_socket).receiving_audio())

                    self.sound_num = int(self.splited_message[1])
                    self.translated_main_data = pk.loads(the_main_data)
                    sf.write("trial"+str(self.num_of_files) +
                             ".wav", self.translated_main_data, self.sound_num)
                    self.textbox.insert(
                        END, self.splited_message[2]+": "+"play audiofile trial"+str(self.num_of_files)+".wav ")
                    self.textbox.bind("<<ListboxSelect>>", self.play_audio)
                    self.num_of_files = self.num_of_files+1
                else:
                    if the_message == "exit!!!exit":
                        break
                    else:
                        self.splited_message = the_message.split("!!!")
                        self.textbox.insert(
                            END, (self.splited_message[2] + ": " + self.splited_message[1]))
            except:
                pass

    def play_audio(self, event):  # playing the voice message
        filename = self.textbox.get(self.textbox.curselection()[0])
        if "play audiofile" in filename:
            filename = filename.split(": ")
            filename = filename[1][15:-1]
            data, fs = sf.read(filename)
            sd.play(data, fs)
            sd.wait()
        else:
            pass


class Voice_Recorder_Window(customtkinter.CTk):
    def __init__(self, username, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")
        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_1, text="record massage", font=(
            "regular", 30))  # font name and size in px
        self.label_1.pack(pady=50, padx=125, ipadx=100)

        # Button to record audio
        record_btn = customtkinter.CTkButton(
            master=self.frame_1, text="Record Audio", command=lambda m=1: Voice_Recorder(self.username, self.client_socket, self.key).threading_rec(m))
        # Stop button
        stop_btn = customtkinter.CTkButton(
            master=self.frame_1, text="Stop Recording", command=lambda m=2: Voice_Recorder(self.username, self.client_socket, self.key).threading_rec(m))
        # Play button
        play_btn = customtkinter.CTkButton(
            master=self.frame_1, text="Play Recording", command=lambda m=3: Voice_Recorder(self.username, self.client_socket, self.key).threading_rec(m))

        send_btn = customtkinter.CTkButton(
            master=self.frame_1, text="Send", command=lambda m=4: Voice_Recorder(self.username, self.client_socket, self.key).threading_rec(m))

        record_btn.pack(pady=10, padx=10)
        stop_btn.pack(pady=10, padx=10)
        play_btn.pack(pady=10, padx=10)
        send_btn.pack(pady=10, padx=10)

        self.mainloop()
