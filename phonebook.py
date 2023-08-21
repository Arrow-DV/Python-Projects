# Phonebook Project <3
# Last Edit 8/13/2023 By Ali Hany Gaber

help = """
[+] Show Users  -1    [+] Edit User   -3         
[+] Add User    -2    [+] Find User   -4           
[+] Remove User -5    [+] Clear Users -6
[+] Export Data -7    # Ali Production                     
"""
def write():
    for x in users:
        with open("Phonebook.txt","a+") as file:
            file.write(f"Name:{x}\nMobile{users[x]}\n")
def edit_user():
    name = input("Old Name: ")
    new_name = input("New Name: ")
    new_mobile = input("New Mobile: ")
    del users[name]
    users[new_name] = new_mobile
def append_user():
    name = input("Name: ")
    phone = input("Mobile: ")

    while phone.isdigit() == False:     
        if phone == "C":
            print("Canceled")   
            break
        print("Invaild Mobile Number Please Try Again.\nType C To Cancel")
        phone = input("Mobile: ")
    else:
        users[name] = phone
        print(f"Added Successfully!\nName:{name}\nMobile:{users[name]}")
def show_users():
    for x in users:
        print(f"Name:{x}\nMobile:{users[x]}")
users = {}
print(help)
while True:
    cmd = input(">>>")
    if cmd == "1":
        show_users()
    elif cmd == "2":
        append_user()

    elif cmd == "3":
        edit_user()
    elif cmd == "4":
        search_name  = input("Put Username: ")
        for z in users:
            if(search_name in z):
                print(f"{z}:{users[z]}")
    elif cmd == "5":
        name = input("User: ")
        del users[name]

    elif cmd == "6":
        users.clear()

    elif cmd == "7":
        write()