username = "GSG"
password = "123456"

def check_username(user):
    return user == username

def check_password(passwd):
    return passwd == password

logfile = "log.txt"
mesg = ""
user = input("Enter the username: ")
while user != "-1":
    if check_username(user):
        mesg = f"{user} is correct"
        passwd = input("Enter the password: ")
        if check_password(passwd):
            mesg = f"{mesg}, also {passwd} is correct\n"
            break
        else:
            mesg = f"{mesg}, but {passwd} is wrong\n"
    else:
        mesg = f"{user} is wrong\n"
    user = input("Enter the username: ")
    with open(logfile, "a") as f:
        f.write(mesg)
        f.close()
    mesg = ""
with open(logfile, "a") as f:
    f.write(mesg)
    f.close()
