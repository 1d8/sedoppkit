import requests

def send(message, dstNumber, apiKey):
    url = "https://secure.smsgateway.ca/SendSMS.aspx?CellNumber={0}&AccountKey={1}&MessageBody={2}".format(dstNumber, apiKey, message)
    response = requests.get(url)
    if response.text == "Message queued successfully":
        return "success"
    else:
        return response.text

