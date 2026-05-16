import tkinter as tk
# login reading from file
def read_file():
    users = {}
    try:
        file = open("users.txt", "r")
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password
        file.close()
    except:
        pass
    return users

def write_file(username, password):
    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()


def login():
    pass

def signup():
    pass    

def main():
    pass

root = tk.Tk()
root.title("Login System")    



root.mainloop()