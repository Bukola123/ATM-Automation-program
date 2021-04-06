import numpy as np

import datetime as dt

np.random.seed(123)

# creating an entry automation or ATM automation

allowedusers = ['First Bank','Access','GT - Bank','Union'] #list of all banks allowed to use the atm machine

allowedpassword = ['1234','passwordsola','passwordtolu','passwordbukola'] #list of password allow

users ={'Ukemelem':{'pin':1234,'balance':12000},'janet':{'pin':3294,'balance':75000},'Sarah':{'pin':8975,'balance':30000}} #Database

users

print ("Welcome to JUMIA PAY \n")

print("  ")

print(dt.datetime.now())

print('Insert card \n')

username = input('Username')  #where the username is automatically detected when the atm card is plug in

pin = int(input("pin"))

userid = users[username]['pin']

balance = users[username]['balance']

print(balance)

if pin == userid:

    print ("Welcome to JUMIA PAY")

    print("")

    print('Select Account type \n')

    print("1" " " 'Savings' '\n')

    print('2 Current \n')

    Account = int(input())

    if Account > 0:

        print("Available Transactions \n")

        print("1" " " 'Deposit \n')

        print('2' " " 'Withdraw \n')

        print ('3' " " 'Transfer \n')

        print('4' " " 'Check Balance \n')

        selectedoption = int(input('please select an option \n'))

        if selectedoption == 1:

            print('You select to Deposit \n')

            print("1" " " '2000' '\n')

            print("2" " " '5000' '\n')

            print("3" " " '10000' '\n')

            print("4" " " '15000' '\n')

            print("5" " " '20000' '\n')

            print("6 others \n")

            deposit = int(input('Amount to Deposit \n'))

            if deposit == 1:

                balance = balance + 2000                

                print(" ")

                print('You are about to save', 2000)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(2000, 'Deposit Successful')

                    print('Available balance', balance)

                else:

                    print('Deposit Cancelled')

            elif deposit == 2:

                balance = balance + 5000                

                print(" ")

                print('You are about to save', 5000)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(5000, 'Deposit Successful')

                    print('Available balance', balance)

                else:

                    print('Deposit Cancelled')

            elif deposit == 3:

                balance = balance + 10000                

                print(" ")

                print('You are about to save', 10000)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(10000, 'Deposit Successful')

                    print('Available balance', balance)

                else:

                    print('Deposit Cancelled')

            elif deposit == 4:

                balance = balance + 15000                

                print(" ")

                print('You are about to save', 15000)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(15000, 'Deposit Successful')

                    print('Available balance', balance)

                else:

                    print('Deposit Cancelled')

            elif deposit == 5:

                balance = balance + 20000                

                print(" ")

                print('You are about to save', 20000)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(20000, 'Deposit Successful')

                    print('Available balance', balance)

                else:

                    print('Deposit Cancelled')

            else:

                balance = balance + deposit                

                print(" ")

                print('You are about to save', deposit)

                print('Please verify your deposit \n')

                print('1 Yes \n')

                print('2 No \n')

                verify1 = int(input())

                if verify1 == 1:

                    print(deposit, 'Deposit Successful')

                    print('Available balance', balance) 

        elif selectedoption == 2:

            print('You select to Withdraw \n')

            print("1" " " '2000' '\n')

            print("2" " " '5000' '\n')

            print("3" " " '10000' '\n')

            print("4" " " '15000' '\n')

            print("5" " " '20000' '\n')

            withdraw = int(input())

            print("Transaction in progress \n")

            if withdraw == 1:

                if 2000 <= balance:

                    balance = balance - 2000

                    print("Take your Cash \n")

                else:

                    print('Insufficient balance \n')

            elif withdraw == 2:

                if 5000 <= balance:

                    balance = balance - 5000

                    print("Take your Cash \n")

                else:

                    print('Insufficient balance \n')

            elif withdraw == 3:

                if 10000 <= balance:

                    balance = balance - 10000

                    print("Take your Cash \n")

                else:

                    print('Insufficient balance \n')                    

            elif withdraw == 4:

                if 15000 <= balance:

                    balance = balance - 15000

                else:

                    print('Insufficient balance \n')                    

            elif withdraw == 5:

                if 20000 <= balance:

                    balance = balance - 20000

                    print("Take your Cash \n")

                else:

                    print('Insufficient balance \n')           

        elif selectedoption == 3:

            print('You select to Transfer \n')

            transfer_account = input("Enter Account No :")                        

            transfer = int(input('Amount'))

            print("Transaction in progress \n")

            if transfer <= balance:

                    balance = balance - transfer

                    print("Transfer Successful")

                    New_transfer = users[transfer_account]['balance'] + transfer

                    users[transfer_account]['balance'] = New_transfer                    

            else:

                print('Insufficient balance \n')

        elif selectedoption == 4:

            print(users[username]['balance'])

    else:

                print('Wrong selection \n')

else:

    print('Wrong Pin, Input a valid pin \n')

    print('Click here to open an account \n')

print('Thank you for banking with us')
