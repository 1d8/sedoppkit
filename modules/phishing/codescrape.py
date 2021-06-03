# Scrapes dead code to be used for obfuscation
from bs4 import BeautifulSoup
import colorama
import requests

# codeTag - programming language to grab code for (EX: GO, Java, Javascript)
# numberOfFunctions - number of functions to grab
def deadGrab(codeTag, numberOfFunctions):
    colorama.init(autoreset=True)
    index = 0
    numberOfFunctions = int(numberOfFunctions)
    h = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    codeTag = codeTag.replace(" ", "+")
    response = requests.get("https://stackoverflow.com/questions/tagged/{0}?tab=newest&pagesize=50".format(codeTag), headers=h)
    if response.status_code != 200:
        print(colorama.Fore.RED + "[!] Error grabbing code! Please ensure your inputted tag is valid!")
    else:
        # We search for question links
        htmlSoup = BeautifulSoup(response.text, "html.parser")
        questionLinks = htmlSoup.find_all("a", class_="question-hyperlink", href=True)
        for link in questionLinks:
            if link.get("href").startswith("/questions/"):
                # If our index isn't equal to the number of functions requested by the user, we grab more
                if index != numberOfFunctions:
                    questionResponse = requests.get("https://stackoverflow.com" + link.get("href"), headers=h)
                    questionHtmlSoup = BeautifulSoup(questionResponse.text, "html.parser")
                    deadCode = questionHtmlSoup.find_all("code")
                    if len(deadCode) != 0:
                        # increase index if we find a function to print
                        index += 1
                        for codeBlock in deadCode:
                            print(colorama.Fore.LIGHTGREEN_EX + codeBlock.text)
                        print(colorama.Fore.RED + "*" * 50)

