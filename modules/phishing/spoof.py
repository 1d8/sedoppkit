import requests
import json
import base64

# opt 1 - receive a reply, sent from message@anonymail.pro
# deprecated
def sendMailOpt1(apiEmail, apiKey, messageStr, toStr):
    # b64encoding apiAuth & creating header
    apiAuth = "{0}:{1}".format(apiEmail, apiKey)
    encodeApiAuth = apiAuth.encode("ascii")
    encodeApi = base64.b64encode(encodeApiAuth).decode("ascii")
    authHeader = {'Authorization': 'Basic {0}'.format(encodeApi)}

    # b64encoding message
    encodeMsg = base64.b64encode(messageStr.encode("ascii")).decode("ascii")
    response = requests.post("https://api.anonymail.pro/v1/emails/option1", headers=authHeader, json={'to':toStr, 'message': encodeMsg})
    responseJson = response.json()
    if responseJson["status"] == "success":
        return "success"
    else:
        return "fail"

# call this after user enters API email & key to verify they are valid, if not ask for them again
# deprecated
def verifyInput(apiEmail, apiKey):
    apiAuth = "{0}:{1}".format(apiEmail, apiKey)
    encodeApi = base64.b64encode(apiAuth.encode('ascii')).decode('ascii')
    authHeader = {'Authorization': 'Basic {0}'.format(encodeApi)}
    response = requests.post("https://api.anonymail.pro/v1/auth", headers=authHeader)
    responseJson = response.json()
    if responseJson["status"] == "success":
        return "success"
    else:
        return "fail"


# deprecated
def sendMailOpt2(apiEmail, apiKey, fromStr, toStr, subjectStr, messageStr):
    # b64encoding apiAuth & creating header
    apiAuth = "{0}:{1}".format(apiEmail, apiKey)
    encodeApiAuth = base64.b64encode(apiAuth.encode("ascii")).decode("ascii")
    authHeader = {'Authorization': 'Basic {0}'.format(encodeApiAuth)}

    # b64 encoding message 
    encodeMsg = base64.b64encode(messageStr.encode("ascii")).decode("ascii")
    # b64 encoding subject
    encodeSubj = base64.b64encode(subjectStr.encode("ascii")).decode("ascii")

    response = requests.post("https://api.anonymail.pro/v1/emails/option2", headers=authHeader, json={'from':fromStr, 'to':toStr, 'subject':encodeSubj, 'message':encodeMsg})
    responseJson = response.json()
    if responseJson["status"] == "success":
        return "success"
    else:
        return "fail"

def sendMail(toEmail, fromEmail, subject, body):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    url = "https://www.phishmail.net/mail.php?sendfrom={0}&sendto={1}&subject={2}&replyto=&msg={3}".format(fromEmail, toEmail, subject.replace(" ", "%20"), body.replace(" ", "%20"))
    response = requests.get(url, headers=headers)
    if response.text == "true":
        return "success"
    else:
        return response.text

