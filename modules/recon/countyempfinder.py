import requests
from bs4 import BeautifulSoup
import re

def findEmployeeEmails(stateAbbrev):
    countyURLs = []
    emailList = []
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    url = "https://www.countyoffice.org/{0}-employee-directory/".format(stateAbbrev)
    response = requests.get(url, headers=headers)
    responseHtml = BeautifulSoup(response.text, "html.parser")
    externalLinks = responseHtml.find_all("a", href=True)
    for i in externalLinks:
        if i.get("href").startswith("http") or i.get("href").startswith("https"):
            countyURLs.append(i.get("href"))
    for i in countyURLs:
        try:
            response = requests.get(i, headers=headers)
        except:
            next
        responseHtml = BeautifulSoup(response.text, "html.parser")
        emails = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", str(responseHtml))
        for addr in emails:
            emailList.append(addr)
    return emailList


