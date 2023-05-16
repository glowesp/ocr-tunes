import time, json, random

def login():
    account = input("do you have an account with ocr-tunes? (y/n) ")
    if account == "y":
        print("redirecting")
        accAccess()
    elif account == "n":
        print("new to ocr-tunes? create an account")
        accCreate()
    else:
        print("invalid option")
        print("please try again")
        login()

""" --WIP
def spotifyConnect():
    spotifyAuth = input("connect to spotify? (y/n) ")
    if spotifyAuth == "y":
        return True
    elif spotifyAuth == "n":
        return False
    else:
        print("error cannot process request")
        print("please try again")
        spotifyConnect()
"""

def openusersfile():
    with open("program/users.json",encoding='UTF-8') as f:
        users = json.loads(f.read())
        return users

def main():
    print("Welcome to ocr-tunes")
    #spotifyConnect() --WIP
    login()

def addAccount(account):
    original = openusersfile()
    original.append(account)
    with open('/workspaces/ocr-tunes/program/users.json','w') as f:
        f.write(json.dumps(original))

def accAccess():
    username = str(input("input your username "))
    password = str(input("input your password "))   

    if auth(username, password):
        print("account found")
        menu()
    else:
        print("no account matches\n try again")
        accAccess()

def accCreate():
    account = {}
    account["user"] = input("input username: ")
    account["password"] = input("input password ")
    account["age"] = int(input("input age: "))
    time.sleep(2)
    print("setting up user preferences...")
    time.sleep(0.5)
    account["fav-genre"] = input("what is your favourite genre? ")
    account["fav-artist"] = input("what is your favourite artist? ")
    time.sleep(0.3)
    print("calculating music based on user preferences...")
    addAccount(account)
    accAccess()

def auth(Name,Password):
    Users = openusersfile()
    for person in Users:
        if (person['user']== Name):
            if (person['pass'] == Password):
                return True


def menu():
    """"""

if __name__ == "__main__":
    main() 
