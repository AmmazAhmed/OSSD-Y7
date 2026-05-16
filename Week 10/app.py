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
    users = read_file()
    user = entry_user.get()
    pwd = entry_pass.get()

    if user in users and users[user] == pwd:
        result.config(text="Login Successful")
    else:
        result.config(text="Wrong Username or Password")


# Signup function
def signup():
    user = entry_user.get()
    pwd = entry_pass.get()
    users = read_file()

    if user in users:
        result.config(text="User Already Exists")
    else:
        write_file(user, pwd)
        result.config(text="Signup Successful")
 

def main():
    global entry_user, entry_pass, result

    tk.Label(root, text="Username").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Password").pack()
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Signup", command=signup).pack()

    result = tk.Label(root, text="")
    result.pack()
root = tk.Tk()
root.title("Login System")    
root.geometry("300x200")


main()
root.mainloop()