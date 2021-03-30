# ATM-Automation-program
A python program that automate how ATM's are function
import datetime as date
allowedusers = ['Charles','John','Mike','Bukola']
allowedpassword = ['1234','2121','2321','2324']
username = input('Username \n')
if username in allowedusers:
    password = input('PIN \n') 
    userid = allowedusers.index(username) 
    if password == allowedpassword[userid]: 
        print ("Welcome to First Bank \n" )
        print(datetime.datetime.now())
        print('1', '' 'Withdraw')
        print('2', '' 'Deposit')
        print('3', '' 'Complaint')
        selectedoption = int(input('Select Option \n'))
        if selectedoption == 1:
            input('How much would you like to withdraw? \n')
            print('Transaction in Progress \n')
            print('Take your Cash \n')
        elif selectedoption == 2:
            deposit = input('How much would you like to Deposit? \n')
            print('Current balace is', '', deposit)
        elif selectedoption == 3:
            input('What issue will you like to report? \n')
            print("Thank you for contacting us")
        print('Thank you for banking with us \n')
    else:
        print('Incorrect Pin, please try again \n')
else:
    print('Invalid login details \n')
