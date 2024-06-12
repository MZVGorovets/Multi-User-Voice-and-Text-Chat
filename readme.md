# Multi-User Voice Chat

## Introduction

Welcome to the Multi-Client Voice and Text Chat project, a client-server application designed to enable real-time secure and efficient communication between users. This project combines various technologies to create a reliable platform for users to communicate.

## Features

- **Encryption:** All messages, whether text or voice, are encrypted using the AES encryption algorithm, also RSA and HASH encryption used for encrypting the AES key(RSA) and password(HASH) encryption before transmission over the network. These encryptions ensure that even if intercepted, the content of the messages will remain secure and cannot be deciphered by unauthorized parties. The encryption mechanism adds a layer of protection to the user's communication, preserving sensitive information and preserving the user's privacy.

- **Real-Time Messaging:** The project provides real-time messaging, ensuring fast communication between users. This feature ensures instant delivery of messages, facilitating efficient and responsive interactions within the platform.

- **Recording and Playback of Audio Files:** In the project, users are provided with a universal communication function - voice messages. With this feature, users can easily record, send, and play audio messages, adding dynamics to their interactions on the platform.

- **Database Integration:** The project provides storage of user credentials using databases. Using databases, the application provides convenient login, giving users convenient and secure access to their accounts.

## Getting Started

1. **Clone the Repository:** Clone the project repository to your local machine.

2. **Requirements:** Copy the contents of `requirements.txt` and paste it into the terminal.

3. **Server Setup:**  Copy the path to the `Server.py` and paste it into the terminal like this: <br> `python PATH\Server.py`<br> If you wish, you can set your own Port like this: <br> `python PATH\Server.py <PORT>`<br> Otherwise the Port will be automatically set to 2000.

4. **Client Setup:** Copy the path to the `Client.py` and paste it into the terminal like this: <br> `python PATH\Client.py`<br> If you wish, you can set your own IP and/or Port like this: <br> `python PATH\Client.py <IP> <PORT>`<br> Otherwise the IP and/or Port will be automatically set to 127.0.0.1(IP) and/or 2000(Port)
