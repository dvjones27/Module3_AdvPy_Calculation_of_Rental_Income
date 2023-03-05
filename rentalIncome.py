# import numpy as np
class returnOnIncome():
    def __init__(self):
        self.finances = []
        self.ttlIncome = []
        self.ttlExpenses = []
        self.ttlCashFlow = []
        self.ttlCashReturn = []
        self.ttlInvestment = []
        
    
    def income(self):
        print("Rental Income Section:".upper())     
        rentalIncome = float(input("Please enter the monthly rental income: $ "))
        self.ttlIncome.append(rentalIncome)
        laundryIncome = float(input("Please enter the monthly laundry income: $ "))
        self.ttlIncome.append(laundryIncome)
        storageIncome = float(input("Please enter the monthly storage income: $ "))
        self.ttlIncome.append(storageIncome)
        miscIncome = float(input("Please enter any other miscellaneous monthly income: $ "))
        self.ttlIncome.append(miscIncome)
        
        return f"The Total Income is: $ {sum(self.ttlIncome):,.2f}."
    
    
    def expenses(self):
        print("Expenses Section:".upper())     
        taxes = float(input("Please input the monthly property taxes: $ "))
        self.ttlExpenses.append(taxes)
        insurance = float(input("Please input the monthly insurance: $ "))
        self.ttlExpenses.append(insurance)
        utilities = float(input("Please input the monthly utilities to include (water/sewage/garbage/electric/gas/other): $ "))
        self.ttlExpenses.append(utilities)
        homeOwners = float(input("Please input the monthly HOA fees: $ "))
        self.ttlExpenses.append(homeOwners)
        yard = float(input("Please input the monthly yard fees to include (lawn care/snow removal): $ "))
        self.ttlExpenses.append(yard)
        vacancy = float(input("Please input the monthly vacancy fees: $ "))
        self.ttlExpenses.append(vacancy)
        repairs = float(input("Please input the monthly repair fees: $ "))
        self.ttlExpenses.append(repairs)
        capEx = float(input("Please input the monthly capital expenditures: $ "))
        self.ttlExpenses.append(capEx)
        propMgmt = float(input("Please input the monthly property management costs: $ "))
        self.ttlExpenses.append(propMgmt)
        mortgage = float(input("Please input the monthly mortgage payments: $ "))
        self.ttlExpenses.append(mortgage)
        
        return f"The Total Expenses are: $ {sum(self.ttlExpenses):,.2f}."
    
    
    def cashFlow(self):
        print("Cash Flow Section:".upper())     
        self.ttlCashFlow = (float(sum(self.ttlIncome)) - float(sum(self.ttlExpenses)))
        # ttlMonthlyCF = (self.ttlCashFlow)
        self.ttlAnnualCF = int(self.ttlCashFlow) * 12
        print(f"The Total Monthly Cash Flow is: $ {self.ttlCashFlow:,.2f}.")
        print(f"The Total Annual Cash Flow is: $ {self.ttlAnnualCF:,.2f}.")
        
    def cashReturn(self):
        print("Cash on Cash Return Section:".upper())     
        downPayment = float(input("Please input the down payment: $ "))
        self.ttlInvestment.append(downPayment)
        closingCosts = float(input("Please input the closing costs: $ "))
        self.ttlInvestment.append(closingCosts)
        rehabBudget = float(input("Please input the rehab budget: $ "))
        self.ttlInvestment.append(rehabBudget)
        miscOther = float(input("Please input any additional miscellaneous costs: $ "))
        self.ttlInvestment.append(miscOther)
        self.ttlInvestment = int(sum(self.ttlInvestment))
        print(f"The Total Investment is: $ {self.ttlInvestment:,.2f}.")
        # print(f'The Total Cash Flow: ${self.ttlCashFlow}')
        # print(f'Cash Return: {self.ttlCashReturn}')
        # print(f'Cash Return {sum(self.ttlCashReturn):,.2f}')
        self.ttlAnnualCF = int(self.ttlCashFlow) * 12
        self.ttlCashReturn = ((self.ttlAnnualCF)/int(self.ttlInvestment)) * 100
        print(f"The Cash on Cash Return is: $ {(self.ttlCashReturn):,.2f}.")  


      
returnOnIncome = returnOnIncome()
print(f'{returnOnIncome.income()}')
print(f'{returnOnIncome.expenses()}')
print(f'{returnOnIncome.cashFlow()}')
print(f'{returnOnIncome.cashReturn()}')