#LoanCalculator.py
#program to calculate monthly mortgage payment
#last edited Sept. 16, 2022 by Alexis C. Monroe CSCI 111 900


#declare variables
address ()                #property address
a = 300000              #amount of the loan, defined as a
b = 0.07                #annual interest rate(entered as a decimal), defined as b
i = 0                   #monthly interest rate
c = 360                 #number of monthly payments, defined as c
m = 0                   #amount of monthly payment, defined as m

#get property address
address = float(input("Please enter the property address (number and street name only):"))

#get amount of the loan
a = float(input("Please enter the amount of the loan (dollars):"))

#get the annual interest rate
b = float(input("Please enter annual interest rate (as a decimal):"))

#get the number of monthly payments
c = float(input("Please enter number of monthly payments:"))

#calculate monthly interest by dividing annual interest rate by 12
i = b/12

#calculate the monthly payment(dollars per month), m = a[i(1+i)^c]/[(1+i)^c-1]
m = a[i(1+i)exp(c)]/[(1+i)exp(c-1)]

#print results - (Amount of the loan) at (annual interest rate) for 12x(number of monthly payments)= amount of monthly payment
print() #blank print to separate input from putput
print("Property Address:", address)
print("The Amount of Your Loan:", a, "dollars")
print("Your Annual Interest Rate:", b )
print("Your Monthly Mortgage Payment:", m, "dollars")
