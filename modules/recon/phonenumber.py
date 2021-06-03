import requests
import random

# TODO:
    # 1. Add more hardcoded API keys

# API KEY LIST
    # abf8e348e6fd1d83dae57347cacc2eb6
    # f1d1b24ae4f6f8f28972dbb14cc12aff
    # f7faa8f91295b618608c2e2730e3b64b
    # 41347f615b9a1ac3790b6c669f4b32c0
    # b390445f540416569a676e8962f5ab09

# number must start with country code (EX: +1)
def validate(number, apiKey):
    if number.startswith("+") != True:
        print("Number must start with country code (EX: +1)!")
        return "no country code"
    apiKeyList = ["abf8e348e6fd1d83dae57347cacc2eb6", "f1d1b24ae4f6f8f28972dbb14cc12aff", "f7faa8f91295b618608c2e2730e3b64b", "41347f615b9a1ac3790b6c669f4b32c0", "b390445f540416569a676e8962f5ab09"]
    if apiKey == "random":
        # choose random api key from our list of hardcoded api keys
        index = random.randint(0, len(apiKeyList)-1)
        url = "http://apilayer.net/api/validate?access_key={0}&number={1}&country_code=&format=1".format(apiKeyList[index], number)
    else:
        url = "http://apilayer.net/api/validate?access_key={0}&number={1}&country_code=&format=1".format(apiKey, number)
    
    response = requests.get(url)
    return response.json()