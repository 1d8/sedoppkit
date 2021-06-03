class Employee:
    def __init__(self, name, year, county, employer, title, payrollType, actualPay, overtimePay, lumpsumPay, totalPay, coworkerList):
        self.name = name
        self.year = year
        self.county = county
        self.employer = employer
        self.title = title
        self.payrollType = payrollType
        self.actualPay = actualPay
        self.overtimePay = overtimePay
        self.lumpsumPay = lumpsumPay
        self.totalPay = totalPay
        self.coworkerList = coworkerList
    
    def Name(self):
        return self.name
    
    def Year(self):
        return self.year

    def County(self):
        return self.county
    
    def Employer(self):
        return self.employer

    def Title(self):
        return self.title
    
    def PType(self):
        return self.payrollType
    
    def Pay(self):
        return self.actualPay
    
    def OTPay(self):
        return self.overtimePay
    
    def LPay(self):
        return self.lumpsumPay

    def TPay(self):
        return self.totalPay

    def Coworkers(self):
        return self.coworkerList