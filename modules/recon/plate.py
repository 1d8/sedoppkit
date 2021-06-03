# scrape https://faxvin.com/license-plate-lookup/ for info on vehicle
# Only works for USA

import requests
from bs4 import BeautifulSoup

def getVehicleInfo(licensePlate, stateAbbrev):
    if len(licensePlate) < 7 or len(stateAbbrev) > 2:
        return "Incorrect length"
    
    url = "https://faxvin.com/license-plate-lookup/result?plate=" + licensePlate + "&state=" + stateAbbrev
    request = requests.get(url)
    requestHtml = BeautifulSoup(request.text, "html.parser")
    vehicleInfo = []

    for i in requestHtml.find_all('b'):
        vehicleInfo.append(i.text)

    return vehicleInfo