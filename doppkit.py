import colorama
import os
from modules.recon import wigle, news, countyempfinder, payroll, ipinfo, businessSearch, plate, businessSearch, venmo, username, phonenumber, wordpress
from modules.annoyance import emailer, smser, caller
from modules.phishing import spoof, codescrape, sms, deadcomment, templateinject
from modules.misc import emailcheck, exploitsearch, passwordgenerator, tempsms, tempmail
from modules.exploitation import csrf, xss, reverseshell
from tabulate import tabulate

# Doesn't exit after 1 tool is finished executing. Returns to main menu
# Should be used instead of main.py

colorama.init(autoreset=True)


def termClear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def exitMessage():
    print(colorama.Fore.WHITE + '''     
  _______ _    _          _   _ _  __ __     ______  _    _ 
 |__   __| |  | |   /\   | \ | | |/ / \ \   / / __ \| |  | |
    | |  | |__| |  /  \  |  \| | ' /   \ \_/ / |  | | |  | |
    | |  |  __  | / /\ \ | . ` |  <     \   /| |  | | |  | |
    | |  | |  | |/ ____ \| |\  | . \     | | | |__| | |__| |
    |_|  |_|  |_/_/    \_\_| \_|_|\_\    |_|  \____/ \____/ 
    ''' + colorama.Fore.RED + '''
  _______ _    _          _   _ _  __ __     ______  _    _ 
 |__   __| |  | |   /\   | \ | | |/ / \ \   / / __ \| |  | |
    | |  | |__| |  /  \  |  \| | ' /   \ \_/ / |  | | |  | |
    | |  |  __  | / /\ \ | . ` |  <     \   /| |  | | |  | |
    | |  | |  | |/ ____ \| |\  | . \     | | | |__| | |__| |
    |_|  |_|  |_/_/    \_\_| \_|_|\_\    |_|  \____/ \____/ 
        ''' + colorama.Fore.WHITE + '''
  _______ _    _          _   _ _  __ __     ______  _    _ 
 |__   __| |  | |   /\   | \ | | |/ / \ \   / / __ \| |  | |
    | |  | |__| |  /  \  |  \| | ' /   \ \_/ / |  | | |  | |
    | |  |  __  | / /\ \ | . ` |  <     \   /| |  | | |  | |
    | |  | |  | |/ ____ \| |\  | . \     | | | |__| | |__| |
    |_|  |_|  |_/_/    \_\_| \_|_|\_\    |_|  \____/ \____/         
        ''' + colorama.Fore.RED + '''
    [Happy Hacking!]''')

def reconToolDisplay():
    print(colorama.Fore.LIGHTCYAN_EX + '''
                                                            `-.
                                                      .`
                                                   _.`.`
                                               _.-` .`
                                       ___.---` _.-`
                               __..---`___..---`
                      _...--.-`   _.--`
                  _.-`.-`.-`  _.-`
               .-` .`  .`   .`
    .         /   /   /    /                    .
    \`-.._    |  |    \    `.              _..-`/
   .'-.._ ``--.._\     `. -- `.      _..-``  _..-`.
   `_    _       `-. .`        `. .-`      _    _`
     `.``           .            \          ``.`
      `-.-'    _   .              :   _   `-.-`
        `..-..'    ;       .` `.  '    `..-..`
            /      .      : .-. : :        \
            `._     \     ;( O ) /      _.`
     LGB       `-._.'`.    .`-'.' `._.-'
                       `-....-`
        ["The quieter you become, the more you can hear."]

        [1] - Critical news search
        [2] - License plate
        [3] - Username search
        [4] - Business keyword search
        [5] - IP addr info
        [6] - County email finder
        [7] - Government employee salary records
        [8] - Venmo Transactions
        [9] - Phone number validator
        [10] - Find SSID location
        [11] - Search for SSIDs
        [12] - Wordpress scanner
    ''' + colorama.Fore.RED + '''
        [Any other number to back up]
    ''')

def exploitationToolsDisplay():
    print(colorama.Fore.LIGHTCYAN_EX + '''
                                                XXXXXXXXX
                                          XXXXXXXXXXXXX
                                        XXXXXXXXXXXXXXXXX
                                       XXXXXXXXXX    XXXXX
      X                                XXXXXXXXXX    XXXXX
 XX   X  X                      XXXXXXXXXXXXXXXXXXXXXXXXXXX
   XX XXX    XXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXX
     XXX XXXXX   XXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   XX XXX           XXX   XX    XXXXXXXXXXXXXXXXXXXXXXXXXXX
 XX   X  XX           XXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXX
      X                                XXXXXXXXXXXXXXXXXXX
                                       XXXXXXXXXXXXXXXXXXX
                                        XXXXXXXXXXXXXXXXX
                                          XXXXXXXXXXXXX
                                            XXXXXXXXX
        [1] - Exploit search
        [2] - CSRF exploit generator
        [3] - XSS payloads
        [4] - Reverse shells
    ''' + colorama.Fore.RED + '''
        [Any other number to back up]''')

def annoyanceToolDisplay():
    print(colorama.Fore.LIGHTCYAN_EX + '''
        ░░░░░░░░░░░░░░░░░░░░
        ░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
        ░█░░░░░░░░▀▄░░░░░░▄░
        █░░▀░░▀░░░░░▀▄▄░░█░█
        █░▄░█▀░▄░░░░░░░▀▀░░█
        █░░▀▀▀▀░░░░░░░░░░░░█
        █░░░░░░░░░░░░░░░░░░█
        █░░░░░░░░░░░░░░░░░░█
        ░█░░▄▄░░▄▄▄▄░░▄▄░░█░
        ░█░▄▀█░▄▀░░█░▄▀█░▄▀░
        ░░▀░░░▀░░░░░▀░░░▀░░░
        
        [Ahh, finally some peace & quiet...]

        [1] - SMS bomber
        [2] - Email bomber
        [3] - Call bomber
    ''' + colorama.Fore.RED + '''
        [Any other number to back up]
    ''')
def phishingToolDisplay():
    print(colorama.Fore.LIGHTCYAN_EX + '''
                                        _H_
                                   /___\
                                   \888/
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~U~^~^~^~^~^~^~^
                      ~              |
      ~                        o     |        ~
                ___        o         |
       _,.--,.'`   `~'-.._    O      |
      /_  .-"      _   /_\'.         |   ~
     .-';'       (( `  \0/  `\       #
    /__;          ((_  ,_     |  ,   #
    .-;                  \_   /  #  _#,
   /  ;    .-' /  _.--""-.\`~`   `#(('\\        ~
   ;-';   /   / .'                  )) \\
       ; /.--'.'                   ((   ))
        \     |        ~            \\ ((
         \    |                      )) `
   ~      \   |                      `
           \  |
      jgs  .` `""-.
         .'        \         ~               ~
         |    |\    |
         \   /  '-._|
          \.'

        [Let's hope they take the bait!]

        [1] - Dead code scraper
        [2] - Dead comment scraper
        [3] - Critical news search for creating lures
        [4] - SMS sender
        [5] - Email sender
        [6] - Template injector
    ''' + colorama.Fore.RED + '''
        [Any other number to back up]
    ''')

def miscToolDisplay():
    print(colorama.Fore.LIGHTCYAN_EX + '''
        [1] - Email validator
        [2] - Exploit search
        [3] - Password generator
        [4] - Temporary SMS
    ''' + colorama.Fore.RED + '''
        [Any other number to back up]
    ''')


def getToolSelection():
    selection = ""
    while isinstance(selection, int) != True:
        try:
            selection = int(input(colorama.Fore.LIGHTCYAN_EX + "Tool Selection: "))
            return selection
        except:
            print(colorama.Fore.RED + "You must enter an integer!")


def moduleDisplay():
    selection = ""
    print(colorama.Fore.BLUE + "\t\t\t\t\t\t\t[Social Engineering Dopp Kit]")
    print(colorama.Fore.LIGHTCYAN_EX + '''\t\t
   ▄████████    ▄████████      ████████▄   ▄██████▄     ▄███████▄    ▄███████▄         ▄█   ▄█▄  ▄█      ███     
  ███    ███   ███    ███      ███   ▀███ ███    ███   ███    ███   ███    ███        ███ ▄███▀ ███  ▀█████████▄ 
  ███    █▀    ███    █▀       ███    ███ ███    ███   ███    ███   ███    ███        ███▐██▀   ███▌    ▀███▀▀██ 
  ███         ▄███▄▄▄          ███    ███ ███    ███   ███    ███   ███    ███       ▄█████▀    ███▌     ███   ▀ 
▀███████████ ▀▀███▀▀▀          ███    ███ ███    ███ ▀█████████▀  ▀█████████▀       ▀▀█████▄    ███▌     ███     
         ███   ███    █▄       ███    ███ ███    ███   ███          ███               ███▐██▄   ███      ███     
   ▄█    ███   ███    ███      ███   ▄███ ███    ███   ███          ███               ███ ▀███▄ ███      ███     
 ▄████████▀    ██████████      ████████▀   ▀██████▀   ▄████▀       ▄████▀             ███   ▀█▀ █▀      ▄████▀   
                                                                                      ▀                          
            [1] - Recon
            [2] - Annoyance
            [3] - Phishing
            [4] - Misc.
            [5] - Exploitation
            [6] - Creator info
            [7] - Credits
    ''' + colorama.Fore.LIGHTRED_EX + '''
            [Any other number to exit]
    ''')
    while isinstance(selection, int) != True:
        try:
            selection = int(input(colorama.Fore.LIGHTCYAN_EX + "Module number: "))
            return selection
        except:
            print(colorama.Fore.LIGHTRED_EX + "You must enter an integer!")

exitVal = False
while exitVal != True:
    moduleSelection = moduleDisplay()
    if moduleSelection == 1:
        # Recon tool section
        termClear()
        reconToolDisplay()
        reconTool = getToolSelection()
        if reconTool == 1:
            # call news module
            #termClear()
            print(colorama.Fore.YELLOW + "Available regions: Ae, Ar, At, Au, Be, Bg, Br, Ca, Ch, Cn, Co, Cu, Cz, De, Eg, Fr, Gb, Gr, Hk, Hu, Id, Ie, Il, In, It, Jp, Kr, Lt, Lv, Ma, Mx, My, Ng, Nl, No, Nz, Ph, Pl, Pt, Ro, Rs, Ru, Sa, Se, Sg, Si, Sk, Th, Tr, Tw, Ua, Us, Ve, Za")
            regionAbbrev = input(colorama.Fore.LIGHTGREEN_EX + "Enter 2 character abbreviation for region to pull news from: ")
            category = input(colorama.Fore.LIGHTGREEN_EX + "Enter category to pull news from (EX: Business, politics, general, science): ")
            articleList = news.retrieveArticles(regionAbbrev, category)
            if articleList == "No results":
                print(colorama.Fore.RED + "Error with your query. Please ensure your region is available & your category isn't too narrow.")
            elif articleList == "Error":
                print(colorama.Fore.RED + "Error with server. Please ensure API key is correct and server is up.")
            else:
                titleTable = [["Article Title"]]
                for i in articleList:
                    titleTable.append([i.Title()])
                print(colorama.Fore.LIGHTCYAN_EX + tabulate(titleTable, headers="firstrow", showindex="always"))        
                exitNews = False
                print(colorama.Fore.RED + "[Enter 99 to exit]")
                while exitNews != True:
                    articleIndex = int(input(colorama.Fore.LIGHTGREEN_EX + "Enter index to expand article info: "))
                    if articleIndex == 99:
                        exitNews = True
                    else:
                        try: 
                            print(colorama.Fore.LIGHTCYAN_EX + '''
                            Published: {0}
                            Description: {1}
                            URL: {2}
                            '''.format(articleList[articleIndex].Date(), articleList[articleIndex].Description(), articleList[articleIndex].URL()))
                        except IndexError:
                            print(colorama.Fore.RED + "Your entered article index was out of range!")
        
        elif reconTool == 2:
            # calls license plate module
            print(colorama.Fore.YELLOW + "[Only works for USA currently]")
            plateNumber = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the plate number: "))
            stateAbbrev = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the state abbreviation: "))
            vehicleInfo = plate.getVehicleInfo(plateNumber, stateAbbrev)
            print(colorama.Fore.LIGHTGREEN_EX + "VIN: {0}\nMake: {1}\nModel:{2}\nYear: {3}\nTrim: {4}\nStyle/body: {5}\nEngine: {6}\nMade in: {7}\nAge: {8}\n".format(vehicleInfo[0], vehicleInfo[1], vehicleInfo[2], vehicleInfo[3], vehicleInfo[4], vehicleInfo[5], vehicleInfo[6], vehicleInfo[7], vehicleInfo[8]))
        elif reconTool == 3:
            # call username module
            targetUsername = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter username: "))
            username.check(targetUsername)
        elif reconTool == 4:
            # call BBB business gather module
            print(colorama.Fore.YELLOW + '''
                [useful for finding business names]
                Only works in USA, CAN, MEX!
            ''')
            businessValidInput = False
            while businessValidInput != True:
                stateAbbrev = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the 2 letter state/territory abbreviation. Leave blank to search entire region: "))
                countryAbbrev = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the 3 letter country abbreviation: "))
                businessCategory = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the business category: "))
                countryAbbrev = countryAbbrev.upper()
                if (stateAbbrev == "" or len(stateAbbrev) == 2) and (countryAbbrev == "USA" or countryAbbrev == "CAN" or countryAbbrev == "MEX"):
                    businessValidInput = True
            table = businessSearch.findBusinessInfo(businessCategory, stateAbbrev, countryAbbrev)
            if table == "error":
                print(colorama.Fore.LIGHTRED_EX + "Error encountered! Ensure spelling & regions are correct!")
            else:
                print(colorama.Fore.LIGHTGREEN_EX + tabulate(table, headers="firstrow"))
        elif reconTool == 5:
            # call IP info module
            ipAddr = input(colorama.Fore.LIGHTGREEN_EX + "Enter IP address: ")
            locationInfo = ipinfo.ipToGeo(ipAddr)
            torData = ipinfo.isTorRelay(ipAddr)
            print(colorama.Fore.LIGHTRED_EX + "[GEOLOCATION INFO]")
            print(colorama.Fore.LIGHTGREEN_EX + tabulate(locationInfo, headers="firstrow"))
            print(colorama.Fore.LIGHTRED_EX + "[TOR INFO]")
            if torData == "no tor info":
                print(colorama.Fore.LIGHTRED_EX + "Not an onion router")
            else:
                print(colorama.Fore.LIGHTGREEN_EX + tabulate(torData, headers="firstrow"))
        elif reconTool == 6:
            # call county employee email finder module
            stateAbbrev = input(colorama.Fore.LIGHTGREEN_EX + "Enter state abbreviation (ex: wa): ")
            resultList = countyempfinder.findEmployeeEmails(stateAbbrev)
            print(colorama.Fore.LIGHTGREEN_EX + "RESULTS:\n{0}".format(resultList))
        elif reconTool == 7:
            # call payroll module
            employeeName = input(colorama.Fore.LIGHTGREEN_EX + "Enter the employee's first & last name: ")
            stateFullValid = False
            while stateFullValid != True:
                stateFull = input(colorama.Fore.LIGHTGREEN_EX + "Enter the full state of the employee (NO ABBREVIATIONS): ")
                if len(stateFull) == 2:
                    print(colorama.Fore.LIGHTRED_EX + "NO ABBREVIATIONS!")
                else:
                    stateFullValid = True
            employeeList = payroll.records(employeeName, stateFull)
            for employee in employeeList:
                print(colorama.Fore.LIGHTGREEN_EX + "Name: {0}\nYear: {1}\nCounty: {2}\nEmployer: {3}\nTitle: {4}\nPayment Type: {5}\nPay: {6}\nOvertime Pay: {7}\nLumpsum Pay: {8}\nTotal Pay: {9}\nCoworker List: {10}\n".format(employee.Name(), employee.Year(), employee.County(), employee.Employer(), employee.Title(), employee.PType(), employee.Pay(), employee.OTPay(), employee.LPay(), employee.TPay(), employee.Coworkers()))
                print(colorama.Fore.LIGHTRED_EX + "*" * 50)
        elif reconTool == 8:
            # call venmo module
            username = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the Venmo username: "))
            result = venmo.payments(username)
            if result == "user not found":
                print(colorama.Fore.LIGHTRED_EX + "{0} was not found! Double check spelling!".format(username))
            else:
                print(colorama.Fore.LIGHTGREEN_EX + tabulate(result, headers="firstrow"))
        elif reconTool == 9:
            # call phone number module
            print(colorama.Fore.YELLOW + "[Uses https://numverify.com/ API for verification. Create an account for an API key or use a hardcoded one]")
            number = input(colorama.Fore.LIGHTGREEN_EX + "Enter phone number (Ensure it starts with the proper country code): ")
            apiKey = input(colorama.Fore.LIGHTGREEN_EX + "Enter API key (Enter random to use a hardcoded API key): ")
            result = phonenumber.validate(number, apiKey)
            if result == "no country code":
                print(colorama.Fore.LIGHTGREEN_EX + "You must enter a country code!")
            else:
                if result["valid"] == True:
                    print(colorama.Fore.LIGHTGREEN_EX + '''Country code: {0}
Location: {1}
Carrier: {2}
Line Type: {3}'''.format(result["country_code"], result["location"], result["carrier"], result["line_type"]))
                else:
                    print(colorama.Fore.LIGHTGREEN_EX + result)
        elif reconTool == 10:
            # call wigle SSID location finder
            print(colorama.Fore.YELLOW + "[Uses Wigle API. Must have API key!]")
            apiKey = input(colorama.Fore.LIGHTGREEN_EX + "Enter Wigle API key: ")
            ssidName = input(colorama.Fore.LIGHTGREEN_EX + "Enter SSID name: ")
            result = wigle.findSSIDLocation(ssidName, apiKey)
            print(colorama.Fore.LIGHTGREEN_EX + tabulate(result, headers="firstrow"))
        elif reconTool == 11:
            # call wigle SSID info searcher
            print(colorama.Fore.YELLOW + "[Uses Wigle API. Must have API key!]")
            apiKey = input(colorama.Fore.LIGHTGREEN_EX + "Enter Wigle API key: ")
            ssidName = input(colorama.Fore.LIGHTGREEN_EX + "Enter SSID name (can include wildcard '%' at end of SSID name): ")
            result = wigle.findSSIDInfo(ssidName, apiKey)
            print(colorama.Fore.LIGHTGREEN_EX + tabulate(result, headers="firstrow"))
        elif reconTool == 12:
            # call wordpress scan
            print(colorama.Fore.YELLOW + "[Great for finding misconfigured WordPress sites!]")
            wpURL = input(colorama.Fore.LIGHTGREEN_EX + "Enter site url: ")
            wordpress.scan(wpURL)

    elif moduleSelection == 2:
        # Annoyance tool section
        termClear()
        annoyanceToolDisplay()
        annoyingTool = getToolSelection()
        if annoyingTool == 1:
            # call sms bomber
            number = input(colorama.Fore.LIGHTGREEN_EX + "Enter phone number: ")
            smser.whioNewsletter(number, 6)
            smser.text4BabyAlert(number)
            smser.misenNewsletter(number)
            for i in range(100):
                smser.subtext(number)
            
        elif annoyingTool == 2:
            # call email bomber
            email = input(colorama.Fore.LIGHTGREEN_EX + "Enter email: ")
            response = emailer.cnnNewsletter(email)
            response = emailer.whoMediaDistrib(email)
            response = emailer.eeNews(email)
            response = emailer.foxNews(email)
            emailer.yoFreeSamples(email)
            response = emailer.dailyMiracle(email)
            for i in range(25):
                response = emailer.worldTribune(email)
        elif annoyingTool == 3:
            # call call bomber
            number = input(colorama.Fore.LIGHTGREEN_EX + "Enter phone number: ")
            for i in range(10):
                caller.callmyphone(number)
                caller.wheresmyphone(number)
                caller.phonemyphone(number)
    elif moduleSelection == 3:
        # Phishing tool section
        termClear()
        phishingToolDisplay()
        phishTool = getToolSelection()

        if phishTool == 1:
            # Call Dead Code grabber
            programmingLang = input(colorama.Fore.LIGHTGREEN_EX + "Enter the language to grab code for (EX: Go, Javascript, etc): ")
            numberOfFunctions = ""
            while isinstance(numberOfFunctions, int) != True:
                try:
                    numberOfFunctions = int(input(colorama.Fore.LIGHTGREEN_EX + "Enter the number of functions to output: "))
                except:
                    print(colorama.Fore.RED + "Please enter an integer!")
            codescrape.deadGrab(programmingLang, numberOfFunctions)
        
        elif phishTool == 2:
            print(colorama.Fore.YELLOW + "[Good for obfuscating VBA!]")
            poemLines = deadcomment.scrape()
            print(colorama.Fore.LIGHTGREEN_EX + "Your dead comments are below:")
            for line in poemLines:
                print(colorama.Fore.LIGHTGREEN_EX + line)
            
        
        elif phishTool == 3:
            print(colorama.Fore.YELLOW + "Available regions: Ae, Ar, At, Au, Be, Bg, Br, Ca, Ch, Cn, Co, Cu, Cz, De, Eg, Fr, Gb, Gr, Hk, Hu, Id, Ie, Il, In, It, Jp, Kr, Lt, Lv, Ma, Mx, My, Ng, Nl, No, Nz, Ph, Pl, Pt, Ro, Rs, Ru, Sa, Se, Sg, Si, Sk, Th, Tr, Tw, Ua, Us, Ve, Za")
            regionAbbrev = input(colorama.Fore.LIGHTGREEN_EX + "Enter 2 character abbreviation for region to pull news from: ")
            category = input(colorama.Fore.LIGHTGREEN_EX + "Enter category to pull news from (EX: Business, politics, general, science): ")
            articleList = news.retrieveArticles(regionAbbrev, category)
            if articleList == "No results":
                print(colorama.Fore.RED + "Error with your query. Please ensure your region is available & your category isn't too narrow.")
            elif articleList == "Error":
                print(colorama.Fore.RED + "Error with server. Please ensure API key is correct and server is up.")
            else:
                titleTable = [["Article Title"]]
                for i in articleList:
                    titleTable.append([i.Title()])
                print(colorama.Fore.LIGHTCYAN_EX + tabulate(titleTable, headers="firstrow", showindex="always"))        
                exitNews = False
                print(colorama.Fore.RED + "[Enter 99 to exit]")
                while exitNews != True:
                    articleIndex = int(input(colorama.Fore.LIGHTGREEN_EX + "Enter index to expand article info: "))
                    if articleIndex == 99:
                        exitNews = True
                    else:
                        try: 
                            print(colorama.Fore.LIGHTCYAN_EX + '''
                            Published: {0}
                            Description: {1}
                            URL: {2}
                            '''.format(articleList[articleIndex].Date(), articleList[articleIndex].Description(), articleList[articleIndex].URL()))
                        except IndexError:
                            print(colorama.Fore.RED + "Your entered article index was out of range!")
        
        elif phishTool == 4:
            print(colorama.Fore.YELLOW + "[Uses smsgateway.ca API Key required! Can verify account with Textnow or another temporary SMS service!]")
            apiKey = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter API key: "))
            message = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter message to send to target: "))
            dstNumber = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the destination phone number: "))
            smsResult = sms.send(message, dstNumber, apiKey)
            if smsResult == "success":
                print(colorama.Fore.LIGHTGREEN_EX + "Message successfully sent to {0}!".format(dstNumber))
            else:
                print(colorama.Fore.LIGHTRED_EX + "Error: {0}".format(smsResult))
        
        elif phishTool == 5:
            # call email spoof module
            print(colorama.Fore.YELLOW + "[Attachments not supported!]")
            toEmail = input(colorama.Fore.LIGHTGREEN_EX + "Enter the target email: ")
            fromEmail = input(colorama.Fore.LIGHTGREEN_EX + "Enter the from email: ")
            subject = input(colorama.Fore.LIGHTGREEN_EX + "Enter the subject line: ")
            body = input(colorama.Fore.LIGHTGREEN_EX + "Enter the body of the message: ")
            spoofResult = spoof.sendMail(toEmail. fromEmail. subject, body)
            if spoofResult == "success":
                print(colorama.Fore.LIGHTGREEN_EX + "Email successfully sent to {0}".format(toEmail))
            else:
                print(colorama.Fore.LIGHTRED_EX + "Error occurred: {0}".format(spoofResult))
        
        elif phishTool == 6:
            # call template inject module
            print(colorama.Fore.YELLOW + "[Need a .docx file with macros? You've come to the right place!]")
            print(colorama.Fore.YELLOW + "[NOTE: You must be hosting your template with the macros somewhere accessible!]")
            templateURL = input(colorama.Fore.LIGHTGREEN_EX + "Enter the URL of the template with macros: ")
            docxPath = input(colorama.Fore.LIGHTGREEN_EX + "Enter the local path to the .docx file: ")
            templateinject.injector(docxPath, templateURL)
            

    elif moduleSelection == 4:
        # Misc Tool Section
        termClear()
        miscToolDisplay()
        miscTool = getToolSelection()
        if miscTool == 1:
            # call email validator
            print(colorama.Fore.YELLOW + "[Great for retrieving data on an email!]")
            email = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter email: "))
            result = emailcheck.isReachable(email)
            print(colorama.Fore.LIGHTGREEN_EX + "Reachable: {0}\nAccepts mail: {1}".format(result["is_reachable"], result["mx"]["accepts_mail"]))
        elif miscTool == 2:
            # call exploit search
            print(colorama.Fore.YELLOW + "[Find a system? Check if it's vulnerable to public exploits for EZaccess!]")
            softwareName = input(colorama.Fore.LIGHTGREEN_EX + "Enter the software name & version if available: ")
            exploitList = exploitsearch.findExploit(softwareName)
            if exploitList == "None":
                print(colorama.Fore.RED + "No results!")
            else:
                for i in exploitList:
                    print(colorama.Fore.LIGHTCYAN_EX + "Exploit ID: {0}, Desc: {1}".format(i.ID(), i.Title()))
                exitExploit = False
                while exitExploit != True:
                    exploitChoice = input(colorama.Fore.LIGHTGREEN_EX + "Enter the exploit ID to view more details [99 to exit]: ")
                    if exploitChoice == "99":
                        exitExploit = True
                    else:
                       for i in exploitList:
                           if i.ID() == exploitChoice:
                               exploitCode = exploitsearch.getCode(exploitChoice)
                               print(colorama.Fore.LIGHTCYAN_EX + '''
Title: {0}
Exploit Type: {1}
Platform: {2}
Published: {3}
Verified Exploit: {4}
Code: {5}
                               '''.format(i.Title(), i.ExploitType(), i.Platform(), i.PublishDate(), i.IsVerified(), exploitCode))

        elif miscTool == 3:
            # call password generator
            validLength = False
            while validLength == False:
                try:
                    passLength = int(input(colorama.Fore.LIGHTGREEN_EX + "Enter length of password: "))
                    validLength = True
                except:
                    print(colorama.Fore.LIGHTRED_EX + "Must enter integer!")
            password = passwordgenerator.generate(passLength)
            print(colorama.Fore.LIGHTGREEN_EX + "Generated password: " + password)
        elif miscTool == 4:
            # call temp sms
            tempSmsExit = False
            availableNumbers = tempsms.getNumbers()
            print(colorama.Fore.LIGHTGREEN_EX + tabulate(availableNumbers, headers="firstrow"))
            number = input(colorama.Fore.LIGHTGREEN_EX + "Choose a number from the above list: ")
            if number.startswith("+"):
                number = number[1:]
            while tempSmsExit == False:
                messages = tempsms.retrieveMsgs(number)
                print(colorama.Fore.LIGHTGREEN_EX + tabulate(messages, headers="firstrow"))
                refresh = input(colorama.Fore.LIGHTGREEN_EX + "Enter 'r' to refresh or anything else to exit: ")
                if refresh != "r" and refresh != "R":
                    tempSmsExit = True
    
    elif moduleSelection == 5:
        # Exploitation tool module
        termClear()
        exploitationToolsDisplay()
        exploitationTool = getToolSelection()
        if exploitationTool == 1:
            # call exploit search
            print(colorama.Fore.YELLOW + "[Find a system? Check if it's vulnerable to public exploits for EZaccess!]")
            softwareName = input(colorama.Fore.LIGHTGREEN_EX + "Enter the software name & version if available: ")
            exploitList = exploitsearch.findExploit(softwareName)
            if exploitList == "None":
                print(colorama.Fore.RED + "No results!")
            else:
                for i in exploitList:
                    print(colorama.Fore.LIGHTCYAN_EX + "Exploit ID: {0}, Desc: {1}".format(i.ID(), i.Title()))
                exitExploit = False
                while exitExploit != True:
                    exploitChoice = input(colorama.Fore.LIGHTGREEN_EX + "Enter the exploit ID to view more details [99 to exit]: ")
                    if exploitChoice == "99":
                        exitExploit = True
                    else:
                       for i in exploitList:
                           if i.ID() == exploitChoice:
                               exploitCode = exploitsearch.getCode(exploitChoice)
                               print(colorama.Fore.LIGHTCYAN_EX + '''
Title: {0}
Exploit Type: {1}
Platform: {2}
Published: {3}
Verified Exploit: {4}
Code: {5}
                               '''.format(i.Title(), i.ExploitType(), i.Platform(), i.PublishDate(), i.IsVerified(), exploitCode))
        elif exploitationTool == 2:
            # call CSRF exploit generator
            url = input(colorama.Fore.LIGHTGREEN_EX + "Enter the target url: ")
            encType = input(colorama.Fore.LIGHTGREEN_EX + "Enter the encoding type (Available: application/x-www-form-urlencoded, multipart/form-data, text/plain): ")
            csrfExit = False
            inputList = []
            method = input(colorama.Fore.LIGHTGREEN_EX + "Method Type: ")
            if method.upper() == "GET":
                htmlPage = csrf.generator([], "GET", encType, url)
            else:
                while csrfExit == False:
                    value = str(input(colorama.Fore.LIGHTGREEN_EX + "Enter the name & value combination for the HTML form in the format 'name:value'. Enter 999 to exit: "))
                    if value == "999":
                        csrfExit = True
                    else:
                        inputList.append(value)
                htmlPage = csrf.generator(inputList, "POST", encType, url)
            print(colorama.Fore.LIGHTGREEN_EX + htmlPage)
        elif exploitationTool == 3:
            # call XSS payload
            payloadTable = xss.payloads()
            print(colorama.Fore.LIGHTGREEN_EX + tabulate(payloadTable, headers="firstrow", showindex="always"))
        elif exploitationTool == 4:
            # call reverse shell generate
            print(colorama.Fore.YELLOW + '''
            [Make sure your listener is ready!]
            ''')
            ipAddr = input(colorama.Fore.LIGHTGREEN_EX + "Enter your IP addr the reverse shell will call back to: ")
            port = input(colorama.Fore.LIGHTGREEN_EX + "Enter the port your listener is listening on: ")
            lang = input(colorama.Fore.LIGHTGREEN_EX + "Enter the language for the reverse shell (Available: bash, php, netcat): ")
            shell = reverseshell.generate(lang, ipAddr, port)
            print(colorama.Fore.LIGHTGREEN_EX + shell)
    elif moduleSelection == 6:
        # Display creator info
        print(colorama.Style.DIM + colorama.Fore.LIGHTGREEN_EX + '''
        https://github.com/1d8

        Thank you for your use of this tool.
        ''')
        exitVal = True
    elif moduleSelection == 7:
        # Display inspiration info
        print(colorama.Style.DIM + colorama.Fore.LIGHTGREEN_EX + '''
        Original idea credit - https://github.com/secanonm/HPomb
        Original idea credit - https://github.com/trustedsec/social-engineer-toolkit
        Some tools selected from - https://github.com/jivoi/awesome-osint
        Wordpress user search thanks to - https://www.gosecure.net/
    ''')
        exitVal = True
    else:
        exitMessage()
        exitVal = True
