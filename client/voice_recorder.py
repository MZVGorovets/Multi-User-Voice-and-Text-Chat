import threading
import time
import queue
import sounddevice as sd
import soundfile as sf
import pickle as pk
from tkinter import messagebox
from message_manipulations import *


class Voice_Recorder():
    # Define the user interface
    # create a window for voice recorder screen
    def __init__(self, username, client_socket, key):
        self.key = key
        self.client_socket = client_socket
        self.username = username

        # Create a queue to contain the audio data
        self.q = queue.Queue()
        # Declare variables and initialise them
        self.recording = False
        self.file_exists = False
        # Label to display app title

    # Fit data into queue
    def callback(self, indata, frames, time, status):  # Fit data into queue
        (self.q).put(indata.copy())

    # Functions to play, stop and record audio
    # The recording is done as a thread to prevent it being the main process
    def threading_rec(self, x):  # function that recognize which operation she must to do
        if x == 1:
            # If recording is selected, then the thread is activated
            t1 = threading.Thread(target=self.record_audio)
            t1.start()
        elif x == 2:
            # To stop, set the flag to false
            global recording
            recording = False
            messagebox.showinfo(message="Recording finished")
        elif x == 3:
            # To play a recording, it must exist.

            if file_exists:
                # Read the recording if it exists and play it

                data, fs = sf.read("trial_uwu.wav", dtype='float32')
                sd.play(data, fs)
                sd.wait()
            else:
                # Display and error if none is found
                messagebox.showerror(message="Record something to play")
        elif x == 4:
            # To play a recording, it must exist.
            if file_exists:
                # Read the recording if it exists and send it
                data, fs = sf.read("trial_uwu.wav")
                main_data = pk.dumps(data)
                send_audiofile = "sound"+'!!!'+str(fs)+"!!!"+self.username
                Message_Manipulations(
                    self.key, self.client_socket).sending_message(send_audiofile)
                time.sleep(2)
                Message_Manipulations(
                    self.key, self.client_socket).sending_audio(main_data)
                # __________________________________________________________________________________________________________________________________________ send voice msg

                print('file sent')
            else:
                # Display and error if none is found
                messagebox.showerror(message="Record something to send")

    # Recording function
    def record_audio(self):  # function that record the message
        # Declare global variables
        global recording
        # Set to True to record
        recording = True
        global file_exists
        # Create a file to save the audio
        messagebox.showinfo(message="Recording Audio. Speak into the mic")
        with sf.SoundFile("trial_uwu.wav", mode='w', samplerate=44100, channels=2) as file:
            # Create an input stream to record audio without a preset time
            with sd.InputStream(samplerate=44100, channels=2, callback=self.callback):
                while recording:
                    # Set the variable to True to allow playing the audio later
                    file_exists = True
                    # write into file
                    file.write(self.q.get())
