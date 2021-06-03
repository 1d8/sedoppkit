import requests
import colorama

colorama.init(autoreset=True)

# [+] - available
# [-] - not available

def check(username):
    ytUrl = "https://youtube.com/user/{0}".format(username)
    headers = ({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    response = requests.get(ytUrl)
    if response.status_code == 404:
        # if 404, account is available
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Youtube")
    else:
        # otherwise, taken
        print(colorama.Fore.LIGHTRED_EX + "[-] Youtube")

    twUrl = "https://twitter.com/{0}".format(username)
    response = requests.get(twUrl, headers=headers)
    if response.text.find("This account doesn’t exist") != -1:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Twitter")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Twitter")
    

    blogSpotUrl = "https://{0}.blogspot.com".format(username)
    response = requests.get(blogSpotUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Blogspot")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Blogspot")

    twitchUrl = "https://twitch.tv/{0}".format(username)
    response = requests.get(twitchUrl, headers=headers)
    if response.text.find("Sorry. Unless you’ve got a time machine, that content is unavailable.") != -1:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Twitch")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Twitch")
    
    tiktokUrl = "https://tiktok.com/@{0}".format(username)
    response = requests.get(tiktokUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Tiktok")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Tiktok")
    
    redditUrl = "https://reddit.com/user/{0}".format(username)
    response = requests.get(redditUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Reddit")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Reddit")

    ebayUrl = "https://ebay.com/usr/{0}".format(username)
    response = requests.get(ebayUrl, headers=headers)
    if response.text.find("not found") != -1:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] eBay")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] eBay")

    pinterestUrl = "https://www.pinterest.com/{0}".format(username)
    response = requests.get(pinterestUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Pinterest")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Pinterest")

    slackUrl = "https://{0}.slack.com/".format(username)
    response = requests.get(slackUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Slack Server")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Slack Server")

    githubUrl = "https://github.com/{0}".format(username)
    response = requests.get(githubUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Github")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Github")

    tumblrUrl = "https://{0}.tumblr.com".format(username)
    response = requests.get(tumblrUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Tumblr")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Tumblr")

    flickrUrl = "https://flickr.com/photos/{0}".format(username)
    response = requests.get(flickrUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Flickr")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Flickr")

    productHuntUrl = "https://producthunt.com/@{0}".format(username)
    response = requests.get(productHuntUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Product Hunt")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Product Hunt")

    vimeoUrl = "https://vimeo.com/{0}".format(username)
    response = requests.get(vimeoUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Vimeo")
    else:
        print(colorama.Fore.LIGHTGREEN_EX + "[-] Vimeo")

    aboutmeUrl = "https://about.me/{0}".format(username)
    response = requests.get(aboutmeUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] about.me")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] about.me")

    cashappUrl = "https://cash.app/${0}".format(username)
    response = requests.get(cashappUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Cashapp")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Cashapp")
    
    soundcloudUrl = "https://soundcloud.com/{0}".format(username)
    response = requests.get(soundcloudUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Soundcloud")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Soundcloud")
    
    coderwallUrl = "https://coderwall.com/{0}".format(username)
    response = requests.get(coderwallUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Coderwall")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Coderwall")
    
    paypalUrl = "https://paypal.com/paypalme/{0}".format(username)
    response = requests.get(paypalUrl, headers=headers)
    if response.text.find("We can’t find this profile") != -1:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Paypal")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Paypal")

    dailymotionUrl = "https://dailymotion.com/{0}".format(username)
    response = requests.get(dailymotionUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Daily Motion")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Daily Motion")

    goodreadsUrl = "https://goodreads.com/{0}".format(username)
    response = requests.get(goodreadsUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Goodreads")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Goodreads")
    
    pastebinUrl = "https://pastebin.com/u/{0}".format(username)
    response = requests.get(pastebinUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Pastebin")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Pastebin")
    
    quoraUrl = "https://www.quora.com/profile/{0}".format(username)
    response = requests.get(quoraUrl, headers=headers)
    if response.status_code == 301:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Quora")
    else:
        print(colorama.Fore.LIGHTGREEN_EX + "[-] Quora")

    imgurUrl = "https://imgur.com/user/{0}".format(username)
    response = requests.get(imgurUrl, headers=headers)
    if response.text.find("We searched high and low, but we couldn’t find the page you're looking for. It may have been moved or deleted, or may never have existed at all.") != -1:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Imgur")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Imgur")

    flipboardUrl = "https://flipboard.com/@{0}".format(username)
    response = requests.get(flipboardUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Flipboard")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Flipboard")
    
    vkUrl = "https://vk.com/{0}".format(username)
    response = requests.get(vkUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] VK")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] VK")
    
    livejournalUrl = "https://{0}.livejournal.com/".format(username)
    response = requests.get(livejournalUrl, headers=headers)
    if response.status_code == 404:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Live Journal")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Live Journal")

    mixUrl = "https://mix.com/{0}".format(username)
    response = requests.get(mixUrl, headers=headers)
    if response.status_code == 302:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Mix")
    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] Mix")