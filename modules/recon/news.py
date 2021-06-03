# scrape news sites for info
# newsapi.org - 5dcccb2c565540eead840b5da01bb623 (api-key)
import requests
import json
from tabulate import tabulate
from modules.recon import ArticleClass

# create list of article objects & return that to main func
# display article titles to user, user copies & pastes title they want, we loop through list titles until we find the correct one
# then we print the details of that specific title

apiKey = "5dcccb2c565540eead840b5da01bb623"
def retrieveArticles(regionAbbrev, category):
    response = requests.get("https://newsapi.org/v2/top-headlines?country={0}&category={1}&apiKey={2}&pageSize=15".format(regionAbbrev, category, apiKey))
    responseJson = response.json()
    if responseJson["status"] != "ok":
        return "Error"
    else:
        if responseJson["totalResults"] == 0:
            return "No results"
        else:
            articles = responseJson["articles"]
            articleObjs = []
            for i in articles:
                obj = ArticleClass.Article(i["publishedAt"], i["title"], i["description"], i["url"])
                articleObjs.append(obj)
            return articleObjs