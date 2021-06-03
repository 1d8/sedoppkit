import requests

# uses https://www.callmylostphone.com/
def callmyphone(number):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '29',
    'Origin': 'https://www.callmylostphone.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.callmylostphone.com/',
    'Cookie': 'ARRAffinity=39473925176cb5f0dfb274deb235bf8b0731b69e9848fa7cb4483644a0a16393; ARRAffinitySameSite=39473925176cb5f0dfb274deb235bf8b0731b69e9848fa7cb4483644a0a16393',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1'
    }
    url = "https://www.callmylostphone.com/"
    response = requests.post(url, data={"recipient": number, "noWhen": "0"}, headers=headers)

# uses http://wheresmycellphone.com/
def wheresmyphone(number):
    headers = {
    'Host': 'wheresmycellphone.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '34',
    'Origin': 'http://wheresmycellphone.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://wheresmycellphone.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
    url = "http://wheresmycellphone.com/"
    response = requests.post(url, data={"noArea": number[0:3], "noNumb": number[3:], "noWhen": "0"})

# uses https://phonemyphone.com
def phonemyphone(number):
    headers = {
    'Host': 'www.phonemyphone.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '185',
    'Origin': 'https://www.phonemyphone.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.phonemyphone.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
    url = "https://www.phonemyphone.com/trial"
    response = requests.post(url, data={"call[number]": number, "call[num_retries]": "10", "call[call_now]": "true", "call[local_time_string]": "", "call[time_zone]": "Arizona", "commit": "I+accept.++Call+me."}, headers=headers)

