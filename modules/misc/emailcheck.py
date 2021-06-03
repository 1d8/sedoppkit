import requests
import json

def isReachable(email):
    headers = ({"User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    response = requests.post("https://ssfy.sh/amaurymartiny/reacher@2cb4ed12/check_email", headers=headers, json={"to_email": email})
    return response.json()


