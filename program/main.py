import time, json, random

def login():
    account = input("do you have an account? (y/n)")
    if account == "Y" or "y":
        print("redirecting")
        accAccess()
    elif account == "N" or "n":
        print("new to ocr-tunes? create an account")
        accCreate()

def spotifyConnect():
    spotifyAuth = input("connect to spotify? (y/n)")
    if spotifyAuth == "Y" or "y":
        return True
    elif spotifyAuth == "N" or "n":
        return False
    else:
        print("error cannot process request")
        print("please try again")
        spotifyConnect()

def openusersfile():
    with open('users.json') as f:
        users = json.loads(f.read())
        return users

def main():
    print("Welcome to ocr-tunes")
    spotifyConnect()
    login()

def accAccess():
    print()

def accCreate():
    print()