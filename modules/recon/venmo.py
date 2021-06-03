import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def payments(username):
    url = "https://venmo.com/{0}".format(username)
    headers = ({"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    unwantedHref = ["Sign Up", "Log In", "Log in", "About", "Security", "Fees & FAQ", "Team", "Blog", "Jobs", "Privacy", "Legal", "Help Center", "Contact", "here"]
    response = requests.get(url, headers=headers)
    table = [["Transact.", "Message", "Date"]]
    if response.status_code == 404:
        return "user not found"
    else:
        responseHtml = BeautifulSoup(response.text, "html.parser")
        paymentList = responseHtml.find_all("div", class_="single-payment content-wrap")
        for payment in paymentList:
            # Each venmo payment has a "story" element which is each individual transaction
            paymentStory = payment.get("onclick")
            paymentStory = paymentStory.split("'")
            paymentStoryUrl = "https://venmo.com{0}".format(paymentStory[1])
            paymentStoryResponse = requests.get(paymentStoryUrl, headers=headers)
            paymentStoryHtml = BeautifulSoup(paymentStoryResponse.text, "html.parser")
            transactionActors = paymentStoryHtml.find_all("a", href=True)
            transactionMessage = paymentStoryHtml.find("div", class_="paymentpage-text m_five_t")
            transactionDate = paymentStoryHtml.find("div", class_="date")
            transactionActorList = []
            # removing any other href links such as links to privacy policies, contact pages, etc
            for actor in transactionActors:
                if actor.text in unwantedHref or actor.text.startswith(" Join"):
                    next
                else:
                    transactionActorList.append("{0}{1}".format(actor.text, actor.get("href")))
            
            # removing duplicates
            for i in transactionActorList:
                if i in transactionActorList:
                    transactionActorList.remove(i)
            # formatting transaction between transaction actors (adding 'paid' in middle)
            transaction = "{0} paid {1}".format(transactionActorList[0], transactionActorList[1])
            table.append([transaction, transactionMessage.text, transactionDate.text])
        
        
        return table
        
        
            
