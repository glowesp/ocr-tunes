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
    with open('users.json',encoding='UTF-8') as f:
        users = json.loads(f.read())
        return users

def main():
    print("Welcome to ocr-tunes")
    #spotifyConnect() --WIP
    login()

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
    """"""

def auth(username, password):
    fileopen = openusersfile()
    for i in fileopen:
        print(i)

def menu():
    """"""

if __name__ == "__main__":
    main() 
