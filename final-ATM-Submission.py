import datetime
import random
print('Welcome to Access Bank \n')

print(datetime.datetime.now(),'\n')

print('******* Access Bank ******* \n')

database = {}  

    
def register():
    first_name = input('First Name: \n')
    last_name = input('Last Name \n')
    pin = int(input('Set Pin \n'))
    account_no = account_gen()
    balance = 0
    database[account_no] = [first_name,last_name,pin,balance]
    print('Account successfully created \n')
    print('Your Account number is :', account_no , 'Available balance :',database[account_no][3])
    transaction(account_no)
    
      
    
def account_gen():
    return random.randrange(1111111111,9999999999)

def transaction(account_no):
        name1 = database[account_no][1]
        name2 =database[account_no][0]
        print(f' Welcome', name1.upper(),name2.upper())
        print('1 Deposit \n')
        print('2 Withdraw \n')
        print('3 Transfer \n')
        print('4 Check balance \n')
        selected_option = int(input())
        if selected_option == 1:
            deposit(account_no)
            print('Deposit successful \n')
            retry()
        elif selected_option == 2:
            withdraw(account_no)
            print('Withdraw successful')
            retry()
        elif selected_option == 3:
            transfer(account_no)
            print('Transfer Successful \n')
            retry()
        elif selected_option == 4:
            check_bal(account_no)
            retry()
        else:
            print('Invalid option selected \n')

def deposit(account_no):
    print('You are about to save \n')
    print('1 5000 \n')
    print('2 10000 \n')
    print('3 15000 \n')
    print('4 20000 \n')
    
    deposit = int(input())
    if deposit == 1:
        balance = database[account_no][3] + 5000
        database[account_no][3] = balance
    elif deposit == 2:
        balance = database[account_no][3] + 10000
        database[account_no][3] = balance
    elif deposit == 3:
        balance = database[account_no][3] + 15000
        database[account_no][3] = balance
    elif deposit == 4:
        balance = database[account_no][3] + 20000
        database[account_no][3] = balance

def withdraw(account_no):
    print('You are about to withdraw \n')
    print('1 5000 \n')
    print('2 10000 \n')
    print('3 15000 \n')
    print('4 20000 \n')
    withdraw = int(input())
    dt_balance = database[account_no][3]
    
    if withdraw == 1:
        if 5000 <= dt_balance:
            balance = database[account_no][3] - 5000
            database[account_no][3] = balance
        else:
            print('Insufficient Fund \n')
    elif withdraw == 2:
        if 10000 <= dt_balance:
            balance = database[account_no][3] - 10000
            database[account_no][3] = balance
        else:
            print('Insufficient Fund \n')
    elif withdraw == 3:
        if 15000 <= dt_balance:
            balance = database[account_no][3] - 15000
            database[account_no][3] = balance
        else:
            print('Insufficient Fund \n')
    elif withdraw == 4:
        if 20000 <= dt_balance:
            balance = database[account_no][3] - 20000
            database[account_no][3] = balance
        else:
            print('Insufficient Fund \n')
            
def trans_receiver(receiver_account,trans_amt):
    print(database)
    balance = database[receiver_account][3] + trans_amt
    database[receiver_account][3] = balance
    
        
def transfer(account_no):
    receiver_account = int(input('Enter account to receive fund \n '))
    dt_balance = database[account_no][3]
    if receiver_account in database:
        trans_amt = int(input('Enter amount to transfer \n'))
        if trans_amt <= dt_balance:
            balance = database[account_no][3] - trans_amt
            database[account_no][3] = balance
            trans_receiver(receiver_account,trans_amt)
            
        else:
            print('Insufficient Fund \n')
    else:
        receiver_bank = input('Enter reciever bank \n')
        trans_amt = int(input('Enter amount to transfer \n'))
        if trans_amt <= dt_balance:
            balance = database[account_no][3] - trans_amt
            database[account_no][3] = balance
            
def check_bal(account_no):
    print('balance')
    balance = database[account_no][3]
    print(balance)
    

def login():
    print(f' Welcome \n')
    account_no = int(input('Enter Account No \n'))
    if account_no in database:
        pin = int(input('Enter Pin \n'))
        if pin == database[account_no][2]:
            transaction(account_no)
        else:
            print('Incorrect detials, account no and password did not match \n')
            print('Try again or Register \n')
    else:
        print('Account not found, try again or create an account \n')
        retry()
        

def retry():
    print('1 continue \n')
    print('2 Logout \n')
    retry = int(input())
    if retry == 1:
        login()
    elif retry == 2:
        logout()
    else:
        print('Invalid option selected \n')

def logout():
    transaction(account_no)
    print('Thanks for your patronage \n')
def start():
    print('1 Login \n')
    print('2 Register \n')
    print('Welcome to Access Bank \n')
    start = int(input())
    if start == 1:
        login()
        
    elif start == 2:
        register()
        retry()
        
    else:
        print('You have selected incorrect option \n')
        start()
        
start()
