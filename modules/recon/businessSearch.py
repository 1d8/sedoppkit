import requests
from bs4 import BeautifulSoup

# category - business category (EX: electrician, technology, air conditioning, auto repair, general contractors, etc)
# stateAbbrev - 2 letter abbreviation
# countryAbbrev - 3 letter abbreviation (only works for USA, CAN, MEX)
def findBusinessInfo(category, stateAbbrev, countryAbbrev):
    table = [["Business Name", "BBB Rating", "Physical Address", "Phone Number"]]
    for page in range(1, 10):
        if len(stateAbbrev) == 0:
            # Search entire region
            url = "https://bbb.org/search?find_country={0}&find_text={1}&page={2}&sort=Relevance".format(countryAbbrev.upper(), category.upper(), str(page))
        else:
            url = "https://bbb.org/search?find_country={0}&find_loc={1}&find_text={2}&page={3}&sort=Relevance".format(countryAbbrev.upper(), stateAbbrev.upper(), category.upper(), str(page))
        headers = ({"User-Agent":
                    "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})

        response = requests.get(url, headers=headers)
        # if we don't get a 200 or we find this error message, we exit since the search params didn't yield any results or we're out of pages to search 
        if response.status_code != 200 or response.text.find("Sorry we didn't find any businesses or charities that match your search") != -1 or response.text.find("We’re sorry, we found no results for") != -1:
            return "error"
        responseHtml = BeautifulSoup(response.text, "html.parser")
        businessNames = responseHtml.find_all("h3", class_="MuiTypography-root Name-sc-12ndgzr-0 euGUJH result-item-ab__name MuiTypography-h4")
        businessPhoneNumbers = responseHtml.find_all("p", class_="MuiTypography-root Phone-sc-1p1gq9f-0 klamaz result-item-ab__phone MuiTypography-body1")
        businessAddresses = responseHtml.find_all("p", class_="MuiTypography-root Address-sc-9uj8rv-0 iIcRHS result-item-ab__address MuiTypography-body1")
        for index in range(len(businessNames)):
            try:
                table.append([businessNames[index].text, businessPhoneNumbers[index].text, businessAddresses[index].text])              
            except IndexError:
                index = index + 1
    return table
