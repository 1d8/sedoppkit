import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

headers = ({"User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})

def isTorRelay(ipAddr):
    yesterday = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
    response = requests.get("https://metrics.torproject.org/exonerator.html?ip={0}&timestamp={1}".format(ipAddr, yesterday), headers=headers)
    responseHtml = BeautifulSoup(response.text, 'html.parser')
    sections = responseHtml.find_all("tr")
    if len(sections) == 0:
        return "no tor info"
    else:
        # remove first index, it's just a header
        sections.pop(0)
        table = [["Timestamp", "IP addr", "Identity Fingerprint", "Nickname", "Is Exit Relay"]]
        for i in sections:
            # splitting it to create a list of the table sects since tabulate requires lists
            sect = i.text.split(" ")
            timestamp = sect[1:3]
            ip = sect[3]
            fingerprint = sect[4]
            nick = sect[5]
            isExitRelay = sect[6]
            table.append([timestamp, ip, fingerprint, nick, isExitRelay])
        return table

def ipToGeo(ipAddr):
    response = requests.get("http://ip-api.com/json/{0}".format(ipAddr), headers=headers)
    responseJson = json.loads(response.text)
    country = responseJson["country"]
    region = responseJson["regionName"]
    city = responseJson["city"]
    zip = str(responseJson["zip"])
    lat = str(responseJson["lat"])
    lon = str(responseJson["lon"])
    isp = responseJson["isp"]
    table = [["Country", "Region", "City", "ISP", "Latitude", "Longtitude"], [country, region, city, isp, lat, lon]]
    return table