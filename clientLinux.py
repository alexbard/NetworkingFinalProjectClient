import socket
import threading
import os
import sys

username = input('Please enter your username: ')

while username == "":
    username = input('Username is empty, try again: ')

server_host = "3.133.55.21"
server_port = 42536
    
# server_host = "localhost"
# server_port = 16000

server_address = server_host, server_port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

# filename = f"{username}_chatlog.txt"

# def open_chatlog(username, filename):
#     if os.path.exists(filename):
#         with open(filename, "r") as file:
#             print(f"--- Chat Log of {username} ---")
#             print(file.read())
#             print("--- End of Chat Log ---")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(username.encode('ascii'))
            elif message == 'LEAVE':
                sys.exit()
            else:
                print(message)
                # with open(filename, "a") as file:
                #     file.write(message + "\n")
        except Exception:
            client.close()
            os.system('clear')
            break

def write():
    try:
        while True:
            counter = 0
            words = input()

            while words == "":
                counter += 1
                words = input()
                if counter >= 2:
                    os.system('clear')
                    words = input()

            message = f'{username}: {words}'
            client.send(message.encode('ascii'))
            # with open(filename, "a") as file:
            #     file.write(message + "\n")
            counter = 0
    except Exception:
        os.system('clear')
        pass

os.system('clear')

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
