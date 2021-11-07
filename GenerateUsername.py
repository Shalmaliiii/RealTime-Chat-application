import random 
def generate_username():
    names = list(open(r"C:\Users\shalm\c files\SocketProgramming\names.txt"))
    username = names[random.randint(0,25487)].split('\n')[0] + str(random.randint(1,1e3))
    return username