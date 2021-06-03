import requests
from bs4 import BeautifulSoup
from modules.recon import EmployeeClass

def records(name, stateFull):
    employeeList = []
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    if name == "all":
        url = "https://openpayrolls.com/search/employees/{0}".format(stateFull)
    else:
        newName = name.replace(" ", "-")
        url = "https://openpayrolls.com/search/{0}/{1}".format(newName, stateFull)
    response = requests.get(url, headers=headers)
    responseHtml = BeautifulSoup(response.text, "html.parser")
    table = responseHtml.find("table")
    for row in table.find_all("td"):
        try:
            employeeLink = "https://openpayrolls.com" + row.find("a", href=True).get("href")
            employeeResponse = requests.get(employeeLink, headers=headers)
            employeeHtml = BeautifulSoup(employeeResponse.text, "html.parser")
            firstSection = employeeHtml.find("section", class_="col-12 my-3 order-7 order-sm-7 sectionBlock")
            employeeYear = firstSection.find_all("td", class_="col-6 col-md-7")[0]            
            employeeName = firstSection.find_all("td", class_="col-6 col-md-7")[1]
            employeeCounty = firstSection.find_all("td", class_="col-6 col-md-7")[3]
            employerName = firstSection.find_all("td", class_="col-6 col-md-7")[4]
            employerLocation = firstSection.find_all("a", class_="font-weight-bold")
            employeeTitle = firstSection.find_all("td", class_="col-6 col-md-7")[6]

            secondSection = employeeHtml.find("section", class_="col-12 my-3 order-11 order-sm-11 sectionBlock")
            payrollType = secondSection.find_all("td", class_="col-6 col-md-7")[0]
            actualPay = secondSection.find_all("td", class_="col-6 col-md-7")[1]
            overtimePay = secondSection.find_all("td", class_="col-6 col-md-7")[2]
            lumpsumPay = secondSection.find_all("td", class_="col-6 col-md-7")[3]
            totalPay = secondSection.find_all("td", class_="col-6 col-md-7")[4]

            thirdSection = employeeHtml.find("section", class_="col-12 my-3 order-last order-sm-last sectionBlock")
            employeeCoworkers = thirdSection.find_all("a", class_="btn-link font-weight-600")
            coworkerList = []
            for i in employeeCoworkers:
                coworkerList.append(i.text)

            employeeObj = EmployeeClass.Employee(employeeName.text, employeeYear.text, employeeCounty.text, employerName.text, employeeTitle.text, payrollType.text, actualPay.text, overtimePay.text, lumpsumPay.text, totalPay.text, coworkerList.text)
            employeeList.append(employeeObj)

        except:
            next
    return employeeList

