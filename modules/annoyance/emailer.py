import requests
import json

# cnn - results in 424
def cnnNewsletter(email):
    headers = {
        'Host': 'audience.cnn.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Content-Length': '2128',
        'Origin': 'https://www.cnn.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.cnn.com/',
        'Sec-GPC': '1',
        'TE': 'Trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    data = {"email":email,"newsletters":["breaking_news","five_things","good_stuff","pop_life","what_matters","reliable_sources","coronavirus","health","point","meanwhile","global_briefing","provoke_persuade","markets_now","keep_watching","btb","nightcap","ten","underscored","five_things_sunday","esp_breaking_news","sleep","events_citizen","royal_news","esp_five_things","fitness","wisdom_project"],"userProfileRequest":{"attributes":{"newsletters":{"acquisition_country":"US","breaking_news_source":"subhub","breaking_news_user_score":"0.80","five_things_source":"subhub","five_things_user_score":"0.80","good_stuff_source":"subhub","good_stuff_user_score":"0.80","pop_life_source":"subhub","pop_life_user_score":"0.80","what_matters_source":"subhub","what_matters_user_score":"0.80","reliable_sources_source":"subhub","reliable_sources_user_score":"0.80","coronavirus_source":"subhub","coronavirus_user_score":"0.80","health_source":"subhub","health_user_score":"0.80","point_source":"subhub","point_user_score":"0.80","meanwhile_source":"subhub","meanwhile_user_score":"0.80","global_briefing_source":"subhub","global_briefing_user_score":"0.80","provoke_persuade_source":"subhub","provoke_persuade_user_score":"0.80","markets_now_source":"subhub","markets_now_user_score":"0.80","keep_watching_source":"subhub","keep_watching_user_score":"0.80","btb_source":"subhub","btb_user_score":"0.80","nightcap_source":"subhub","nightcap_user_score":"0.80","ten_source":"subhub","ten_user_score":"0.80","underscored_source":"subhub","underscored_user_score":"0.80","five_things_sunday_source":"subhub","five_things_sunday_user_score":"0.80","esp_breaking_news_source":"subhub","esp_breaking_news_user_score":"0.80","sleep_source":"subhub","sleep_user_score":"0.80","events_citizen_source":"subhub","events_citizen_user_score":"0.80","royal_news_source":"subhub","royal_news_user_score":"0.80","esp_five_things_source":"subhub","esp_five_things_user_score":"0.80","fitness_source":"subhub","fitness_user_score":"0.80","wisdom_project_source":"subhub","wisdom_project_user_score":"0.80"}}},"emailAddress":email}
    response = requests.post("https://audience.cnn.com/newsletters/api/1/subscriptions/add", headers=headers, json=data)
    return response.status_code


def whoMediaDistrib(email):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://confirmsubscription.com/h/d/18DFE0FD1CC9DA69',
        'Content-Type': 'application/json',
        'Origin': 'https://confirmsubscription.com',
        'Content-Length': '204',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    data = {"fields":[{"id":"fieldName","type":"Text","value":["SE Drop Kit by 1d8"]},{"id":"fieldEmail","type":"Email","value":[email]}],"referrer":"https://www.who.int/news-room/newsletters","reCaptchaResponse":0}
    response = requests.post("https://confirmsubscription.com/t/d/HostedSubscribeForm/giylui/", headers=headers, json=data)
    return response.status_code

def dailyMiracle(email):
    url = "https://cloud.m.jesus.net/subscribeAMED"
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ADRUM_BTa=R:38|g:6d51e1b2-495d-43b9-bb71-1d5e88ac61a6; ADRUM_BT1=R:38|i:174|e:272',
    'Content-Length': '410',
    'Origin': 'https://jesus.net',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://jesus.net/a-miracle-every-day/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1'
    }
    response = requests.post(url, data={"firstname": "SE", "lastname": "DOPPKIT", "email": email.replace("@", "%40"), "language": "en", "campaignid": "7013X0000015K1rQAE", "thankyouurl": "https://jesus.net/a-miracle-every-day/confirmation-page-a-miracle-every-day/", "errorurl": "https://miracle.jesus.net//?error=Note:%20Not%20all%20required%20fields%20have%20been%20entered.", "formurl": "https://jesus.net/a-miracle-every-day/", "processform": "Submit"}, headers=headers)
    return response.status_code

# can be submitted multiple times for multiple emails
def worldTribune(email):
    url = "https://worldnewstribune.us5.list-manage.com/subscribe/post?u=cecd6859a856acadd861aa673&id=65c3d2f14e"
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.worldtribune.com/sign-daily-alerts/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '48',
    'Origin': 'https://www.worldtribune.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Cookie': '_abck=E152E85205B67D7332F6E72C257146AB~0~YAAQDC0tFyXLoKF5AQAADuWeogW0TKgCChdQj448j+e/CQivdwdblESQ/6rXHn3pUmtK4/K4mzl0vMHkOZ65zBT9oijHqYhXu1Uj1TH64rMY3HCbGRfQ7nA8R/WGKCkM9nSf6akJ2s8XdmwoP4JI9u/f7ptiZvNUevwa3VV8L0P1uQKzCB3MRsbeQ1iDqZKff82rvWUj3CZD9ZyL/KvXyVDtEaHfygPF/nxF1MZy/TCzU6AYHkQGGbiuymYLWbD6CQUwWFKgP1QrOnaL5vXmzDx+KcEVCAH/DbdJ4G0kOh0z66Up2/CV2FgW74P4qIXrcj7lssPM6ZQkC76ErK30tyV8eL8IU6EY/XEAt2iWcNQ4p08E+NQR8LqBqWG/JYRuDZdeKD1zCGoWux3//F3atW23WgxjmrzTrxzopXA=~-1~-1~-1; _mcid=1.671d4c4e3c24f06b8a6ab7e3a68874c3.e2febfa8cb99ae9456b7c550deab3d1ed8a7cdfc3b16b0a52deadf6330f5eb6b; ak_bmsc=5178DD092B3B241264B8D571E5046603172D2D0C67380000F0B3AC600A967861~pls1hBu0DZFHy+uhlRGsv+ePk7pWgm1C22yO/42lme82JEzi/NJ+9hcgXEYU8Dnfk13Jd3vIE/FopPvFVpw2LxN3Tp8lcuV8ZGWrx0pe6FND5/FkOyltZHSz+Q+h2PqdbgqbwskvZEXVKtxYaB9Uawj0p9afQJDifDMgBGf/p+xBETHVqXJ4LMWJNKPqgrIR3s7qmiAOXQjCGHLjfEx9PR88xOFZ9vCcflGey6IApCfj27YVI9I01I/FSvVD+7znD2; bm_sz=BC866D98141FFB1AA33C36895E0D51E3~YAAQDC0tFybLoKF5AQAADuWeogvxpx3LYfUTcVDuSpFIQl2ZdxcPGgQiYOKpq58WKe0tTxN5j9eVzherMUJd5RU8Qz4ARpIZmx+aU6LpQc4DWz1UqtHrk398MP/jljRu+MumA8SEN4c6hmTF30tA+NCGXDsGZFXboE7dYwkyYDOiKZoJGc/GsP9farPyrP2gw3vrAL5FP8x9RfCz7c9iTupENaSZr6AXYZC8MzU9vyTEOJjde58ckdmYKvqQMP2eChzHQw==; bm_sv=D652D02AACC552237EC642DCE5125072~rGmsKu2g4U8L92j/CkJjBlEgjk/NeDx3QXy6yai2dYyNiWXUwDsWwRE4beLOWevvQAP0O+JIVU9PwzD3SPwq8UG1bCYfwXhoNbMQgzvfV8IaMKvtmrV96+UsK/5JcSdvrpOhOx22q8gR1ZY8FPJw9C2S8dq2fX7Pp9hwAlx7Z2Q=',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
    }
    response = requests.post(url, data={"EMAIL": email, "subscribe": "Subscribe"}, headers=headers)
    return response.text

def yoFreeSamples(email):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://yofreesamples.com/email/',
    'DNT': '1',
    'Connection': 'keep-alive'
    }
    response = requests.get("https://yofreesamples.us3.list-manage.com/subscribe/post-json?u=69af817f1da9d8722e50198ed&id=da2590103e&c=jQuery19008924759121828565_1621931487987&EMAIL={0}&group[9789][2]=2&group[9789][1]=1&SOURCE=popover&MEDIUM=popover&CAMPAIGN=popover&TERM=&b_69af817f1da9d8722e50198ed_da2590103e=&subscribe=Subscribe&_=1621931487988".format(email), headers=headers)


# returns json {"ok": true}
def foxNews(email):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '61',
    'Origin': 'https://www.foxnews.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.foxnews.com/newsletters',
    'Cookie': '_csrf=qe_YFDXlitUBseXqrbVFOni3; AKA_A2=A; usprivacy=1---; FXN_flk=1; AMCV_17FC406C5357BA6E0A490D4D%40AdobeOrg=2121618341%7CMCIDTS%7C18773',
    'Sec-GPC': '1',
    'TE': 'Trailers',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
    url = "https://www.foxnews.com/portal/newsalertsubscribe"
    alertTypes = ["3DC725E303A24F8DBA8D7ED90EFD2033", "3DC725E303A24F8D106D04335B030A1E", "3DC725E303A24F8D7457D18811A93C18", "3DC725E303A24F8DE8DB8BD2CA76E43D", "3DC725E303A24F8DB2CE37CF687DE56B", "3DC725E303A24F8D2F397E652DAD2AE6", "3DC725E303A24F8D0E2C21B39073C09B", "3DC725E303A24F8D8BF986F69AEAACEA", "3DC725E303A24F8D10BFA69067B1CAC9"]
    for alert in alertTypes:
        response = requests.post(url, data={"email": email, "slids": alert})
    return response.text

# returns json - {"followUpUrl": "https://www.eenews.net/get_access/success"}
def eeNews(email):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '625',
    'Origin': 'https://go.politico.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://go.politico.com/index.php/form/XDFrame',
    'Cookie': '__cf_bm=8169c78e484b07a50cacf2a59b590ef3fd372c60-1621932566-1800-AY7uocSeqcGBS5NIqQoxlRRPtjZDeen1Q2rBUBXqrqo384XiSYhQO0PKEr+0n3MVlW9sCJ98JHhydqTV5b6wzws=; BIGipServersj16web-nginx-app_https=!5x7IWbLPOmkEB1SmfApvaf9MEhiEHcTjPPuwWcMBS7zJQchf5ZFTOOz2a/LFA+l4Xy3yZ3sYg+neaSc=',
    'Sec-GPC': '1',
    'TE': 'Trailers',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
    url = "https://go.politico.com/index.php/leadCapture/save2"
    response = requests.post(url, data={"FirstName": "SE", "LastName": "DOPPKIT", "Email": email, "Phone": "0000000000", "Title": "SE DOPP KIT", "Company": "Independent", "Domain_c": "", "PostalCode": "", "Country": "United States", "whatbringsyoutoEENews": "Request a trial", "BakerV2__URL__c": "", "optInRollup": "", "formid": "2133", "munchkinId": "966-KHF-533", "_mkt_trk": "", "formVid": "2133", "_mktoReferrer": "https://www.eenews.net/get_access", "checksumFields": "FirstName,LastName,Email,Phone,Title,Company,Domain__c,PostalCode,Country,whatbringsyoutoEENews,BakerV2__URL__c,optInRollup,formid,munchkinId,_mkt_trk,formVid,_mktoReferrer", "checksum": "08c6bb169a4ca06bb640f73f0071b4e3214f28a98d6fb07668990719b890d0a8"}, headers=headers)
    return response.text
