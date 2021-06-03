import requests
import json
import random

def generateEmail(emailUsername):
    headers = ({"User-Agent":
                    "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    domains = ["getnada.com", "abyssmail.com", "boximail.com", "clrmail.com", "dropjar.com", "getairmail.com", "givmail.com", "inboxbear.com", "robot-mail.com", "tafmail.com", "vomoto.com", "zetmail.com"]
    domainRand = random.randint(0, len(domains)-1)
    response = requests.get("https://getnada.com/api/v1/inboxes/" + emailUsername + "@" + domains[domainRand], headers=headers)
    data = response.json()
    messageMap = data["msgs"]
    return messageMap