import random
import socket
import threading

host = "localhost"
port = 49151
client = 0
address = (host,port)
clients, alias = [],[]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen()

def remove_user(check, name):
    if name in alias:
        pos = alias.index(name)
        user = clients[pos]
        clients.remove(user)
        if check == "kick":
            user.send('You were kicked by the admin.'.encode('ascii'))
        else:
            user.send("Sorry, you can't join this room anymore.".encode('ascii'))
        user.close()
        alias.remove(name)
        if check == "kick":
            broadcast(f"{name} was kicked.".encode('ascii')) 
        else:
            broadcast(f"{name} was banned.".encode('ascii')) 
            

def broadcast(message):
    for user in clients:
        user.send(message)

def connections(client):
    while True: 
        try:
            temp = data = client.recv(1024)
            if temp.decode('ascii').startswith('kick'):
                if alias[clients.index(client)] == 'admin':
                    name = temp.decode('ascii')[5:] 
                    remove_user("kick",name)
                else:
                    client.send("You are not an admin.".encode('ascii'))
            elif temp.decode('ascii').startswith('ban'):
                if alias[clients.index(client)] == 'admin':
                    name = temp.decode('ascii')[4:] 
                    remove_user("ban",name)
                    with open(r'C:\Users\shalm\c files\SocketProgramming\banned_users.txt', 'a') as f:
                        f.write(f'{name}\n')
                    print(f'{name} was banned.')
                else:
                    client.send("You are not an admin.")
            else:
                broadcast(data) 
        except:
            position = clients.index(client)
            clients.remove(client)
            client.close()
            name = alias[position]
            broadcast(f"{name} has left the chat.".encode('ascii'))
            print(f"{name} disconnected.")
            alias.remove(name)
            break
                
def listening():
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}.")
        
        client.send('request'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        
        with open(r'C:\Users\shalm\c files\SocketProgramming\banned_users.txt', 'r') as f:
            ban = f.readlines()
        
        if name+'\n' in ban:
            client.send('ban'.encode('ascii'))
            client.close()
            continue
        
        alias.append(name)
        clients.append(client)

        print(f"{name} connected.")

        if name == 'admin':
            broadcast("Admin joined the chat!".encode('ascii'))
        else:
            broadcast((name + greetings[random.randrange(0,7)] ).encode('ascii'))

        client.send('Connected to server.'.encode('ascii'))

        thread = threading.Thread(target = connections, args=(client,))
        thread.start() 

greetings = [" just joined the server!",", we hope you bought pizza!", " just landed!", " just slid into the server!", " is here, as the prophecy foretold!", " just showed up!",
" hopped into the server!"]

print("Server is listening ...")
listening() 

