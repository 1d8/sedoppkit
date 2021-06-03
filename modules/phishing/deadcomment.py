import requests
import random

def scrape():
    poetList = requests.get("https://poetrydb.org/author").json()
    poetList = poetList["authors"]
    poetIndex = random.randint(0, len(poetList)-1)
    # poetList[poetIndex] - randomly chosen poet from JSON list returned by poetList var
    poetsWork = requests.get("https://poetrydb.org/author/{0}".format(poetList[poetIndex])).json()
    # choose random poem index from randomly chosen poet
    poemIndex = random.randint(0, len(poetsWork)-1)
    return poetsWork[poemIndex]["lines"]
    
