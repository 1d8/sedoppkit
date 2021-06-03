import requests
from tabulate import tabulate

# use % for wildcard (EX: if you want only SSIDs that start with NETGEAR then you'd enter NETGEAR%)
def findSSIDInfo(ssidName, apiKey):
    url = "https://api.wigle.net/api/v2/network/search?onlymine=false&freenet=false&paynet=false&ssidlike={0}".format(ssidName)
    headers = {"Authorization": "Basic {0}".format(apiKey)}
    response = requests.get(url, headers=headers).json()
    resultList = [["Coordinates", "SSID", "SSID Type", "Encryption Type", "Location"]]
    if response["success"] == True:
        # continue on with gathering data
        results = response["results"]
        for result in results:
            coordinates = str(result["trilat"]) + " " + str(result["trilong"])
            ssid = str(result["ssid"])
            ssidType = str(result["type"])
            encryptionType = str(result["encryption"])
            location = "{0} {1}\n{2} {3}\n{4} {5}".format(str(result["road"]), str(result["housenumber"]), str(result["city"]), str(result["postalcode"]), str(result["region"]), str(result["country"]))
            resultList.append([coordinates, ssid, ssidType, encryptionType, location])
        return resultList
    else:
        return "error"

# find SSID location when given an exact SSID
def findSSIDLocation(ssidName, apiKey):
    url = "https://api.wigle.net/api/v2/network/search?onlymine=false&freenet=false&paynet=false&ssidlike={0}".format(ssidName)
    headers = {"Authorization": "Basic {0}".format(apiKey)}
    response = requests.get(url, headers=headers).json()
    resultList = [["SSID name", "coordinates", "MAC addr"]]
    if response["success"] == True:
        results = response["results"]
        for result in results:
            ssidName = str(result["ssid"])
            location = str(result["trilat"]) + " " + str(result["trilong"])
            networkID = str(result["netid"])
            resultList.append([ssidName, location, networkID])
        return resultList
    else:
        return "error"