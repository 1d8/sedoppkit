import requests
from bs4 import BeautifulSoup

def getNumbers():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    response = requests.get("https://receive-smss.com/", headers=headers)
    responseHtml = BeautifulSoup(response.text, 'html.parser')
    numbers = responseHtml.find_all("h4", class_="number-boxes-itemm-number")
    availableNumbers = [["Numbers"]]
    for i in numbers:
        i = i.text[1:] # Removing the + in front of all numbers
        availableNumbers.append([i])
    
    return availableNumbers

def retrieveMsgs(number):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    url = "https://receive-smss.com/sms/{0}".format(number)
    response = requests.get(url, headers=headers)
    responseHtml = BeautifulSoup(response.text, 'html.parser')
    table = [["Sender", "Timestamp", "Message"]]
    for tr in responseHtml.find_all("tr")[1:]:
        tds = tr.find_all("td")
        sender = tds[1].text
        message = tds[4].text
        
        # removing excess data from timestamp
        realMsgIndex = tds[3].text.find("real") 
        timestamp = tds[3].text[0:realMsgIndex]
        
        table.append([sender, timestamp, message])

    return table




