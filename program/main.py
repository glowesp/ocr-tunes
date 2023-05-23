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
    with open('/workspaces/ocr-tunes/users.json',encoding='UTF-8') as f:
        users = json.loads(f.read())
        return users
    
def openplaylistfile():
    with open('/workspaces/ocr-tunes/program/playlists',encoding='UTF-8') as f:
        plist = json.loads(f.read())
        return plist

def main():
    print("Welcome to ocr-tunes")
    #spotifyConnect() --WIP
    login()

def addAccount(account):
    original = openusersfile()
    original.append(account)
    with open('/workspaces/ocr-tunes/users.json','w') as f:
        f.write(json.dumps(original))

def accAccess():
    username = str(input("input your username "))
    password = str(input("input your password "))   

    if auth(username, password):
        print("you are logged in")
        menu()
    else:
        print("no account matches\n try again")
        accAccess()

def accCreate():
    account = {}
    account["user"] = input("input username: ")
    account["password"] = input("input password: ")
    account["age"] = int(input("input age: "))
    time.sleep(2)
    print("setting up user preferences...")
    time.sleep(0.5)
    account["fav-genre"] = input("what is your favourite genre? ")
    account["fav-artist"] = input("what is your favourite artist? ")
    time.sleep(0.3)
    print("calculating music based on user preferences...")
    addAccount(account)
    print("login")
    accAccess()

def auth(Name,Password):
    Users = openusersfile()
    useraccept = False
    passaccept = False
    for person in Users:
        if (person['user']== Name):
            useraccept = True
    for person in Users:
        if (person['password'] == Password):
            passaccept = True
    if useraccept and passaccept:
        return True
        

def menu():
    
    option = int(input("\n1. search for songs\n2. playlist creator\n3. display songs (local)\n"))
    if option == 1:
        print("WIP")
    elif option == 2:
        print("WIP")
    elif option == 3:
        print("display local songs")
        plist = openplaylistfile()
        print(plist)
    else:
        print("option not found.")
        menu()



















if __name__ == "__main__":
    main() 
