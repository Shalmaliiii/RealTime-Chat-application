import time
import socket
import threading
from PasscodeEncryption import *
from GenerateUsername import generate_username

host = "localhost"
port = 49151
client = 0
address = (host,port)
stop_Thread = False

print("Welcome to the chat room!")
alias = input("Enter Alias : ")
if alias == 'admin':
    tries = 3
    entry = False
    while(not(entry) and tries):
        tries -= 1
        pas = input("Passcode : ")
        if  hash(pas) == stored(): 
            entry = True
            print("You've has entered the chat!\nGranting privilages ...")
            time.sleep(1)
            break
        else :
            if tries:
                print(f"You have {tries} tries left!")
    if (not(entry)):
        print("Sorry you aren't the administrator.\nGenereating temperory alias ... ")
        time.sleep(1)
        alias = generate_username()
        print(f"Alias : {alias}")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

def listen():
    while True: 
        global stop_Thread
        if stop_Thread:
            break
        try:
            data = client.recv(1024).decode('ascii')
            if data == 'request':
                client.send(alias.encode('ascii'))
                hear = client.recv(1024).decode('ascii')
                if hear == 'ban':
                    print("[BANNED] Connection refused.")
                    client.close()
            else: 
                print(data)
        except:
            print("[ERROR]")
            client.close() 
            break

def send():
    while True:
        if stop_Thread:
            break
        data = f'{alias} : {input("")}'
        if data[len(alias)+3]=='/':
            if alias == 'admin':
                if data[len(alias)+3:].startswith('/kick'):
                    client.send(f"kick {data[len(alias)+9:]}".encode('ascii'))
                elif data[len(alias)+3:].startswith('/ban'): 
                    client.send(f"ban {data[len(alias)+8:]}".encode('ascii'))       
            else:
                print("Only Admin has permission to execute commands.")
        else:             
            client.send(data.encode('ascii'))
        
receive_thread = threading.Thread(target=listen)
receive_thread.start()

write_thread = threading.Thread(target=send)
write_thread.start() 