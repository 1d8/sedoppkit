import random

def generate(passLength):
    availChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-[]}{\\|;:.,/"
    password = ""
    for i in range(0, passLength):
        randChar = random.randint(0, len(availChars)-1)
        password = password + availChars[randChar]
    return password
