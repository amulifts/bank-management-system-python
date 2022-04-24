import json
import subprocess as sp
from time import sleep, time
with open('accounts.json') as f:
    data=json.load(f)

def clear():
    tmp = sp.call('cls',shell=True)
def new_user():
    #Taking the new users name
    new_data={}
    name=""
    checker_name = 0
    while checker_name!=1:
        first_name=input("Enter your First name: ")
        middile_name=input("Enter your Middle name(Leave empty if none): ")
        last_name=input("Enter your Last name: ")
        if len(middile_name) == 0:
            name=first_name+" "+last_name  
        else:
            name=first_name+" "+middile_name+" "+last_name
        name_checker=list(name)
        for i in range(len(name_checker)):
            asci_val=ord(name_checker[i])
            if (asci_val<=90 and asci_val>=65) or (asci_val<=122 and asci_val>=97) or asci_val==32:
                checker_name=1
            else:
                checker_name=0
                print("Invalid Input!! Enter Your name again: \n")
                break
    if checker_name==1:
        new_data['name']=name
    print(f"Welcome {name} to the Bank of TBC\n")
    #taking the new users pin
    checker_PIN =0
    account_PIN_enter=0000
    while checker_PIN!=1:
        account_PIN_enter=int(input("Enter you 4 digit PIN: "))
        account_PIN_checker=int(input("Re-enter you 4 digit PIN: "))
        if account_PIN_enter==account_PIN_checker:
            if account_PIN_enter>999 and account_PIN_enter<10000:
                    checker_PIN=1
            else:
                checker_PIN=0
                print("PIN must be 4 Digit and cannot start with 0! Enter the Pin again: \n")
        else:
            checker_PIN=0
            print("Entered PIN does not match! Enter the Pin again: \n")
    if checker_PIN==1:
        new_data['PIN']=account_PIN_enter

    #creating the acc number
    account_number=len(data['people'])+1
    new_data['acc_number']=account_number
    print(f"\nYour account number is: {account_number}")

    #setting the default accont balance at 0
    account_balance=0
    new_data['acc_balance']=account_balance
    print(f"\nYour account balance is: {account_balance}")
    sleep(5)
    #entering the data to the json file
    data['people'].append(new_data)
    with open('accounts.json','w') as f:
        json.dump(data,f,indent=2)

def existing_user():  
    if len(data['people'])>0:  
        num=0
        while True:
            check_acc_num=int(input("Please enter your Account Number: "))
            for i in range(len(data['people'])):
                if check_acc_num==data['people'][i]['acc_number']: 
                    num=i
                    break
            if i ==len(data['people']) and check_acc_num != data['people'][i-1]['acc_number']:
                print("Invalid Account Number!!")
            if check_acc_num==data['people'][num]['acc_number']: 
                break


        accountdetails=data['people'][num]
        name=accountdetails['name']
        print(f"Welcome {name}\n")


        while True:    
            check_PIN_1=int(input("Enter Your PIN : "))
            if check_PIN_1==accountdetails['PIN']:
                check_PIN_2=int(input("Re-enter Your PIN : "))
                if check_PIN_2==check_PIN_1:
                    print("PIN is correct!")
                    break
                else:
                    print("The PINs do not match!")
            else:
                print("Incorrect PIN!")
        
        while True:
            clear()
            print(f"Welcome {name} to the Bank of TBC\n")
            choice2=int(input("\n1. View Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Profile\n6. Logout\n"))
            if choice2==1:
                clear()
                balance=accountdetails['acc_balance']
                print(f"Your Account Balance is: {balance}")
                sleep(4)

            elif choice2==2:
                clear()
                enter_amount=int(input("Enter the amount you want to deposit: "))
                new_balance=accountdetails['acc_balance']+enter_amount
                data['people'][num]['acc_balance']=new_balance
                with open('accounts.json','w') as f:
                    json.dump(data,f,indent=2)
                print(f"Amount of Rs. {enter_amount} has been credited to your account!")
                print(f"Your Balance is: {new_balance}")
                sleep(3)

            elif choice2==3:
                while True:
                    clear()
                    enter_amount=int(input("Enter the amount you want to withdraw: "))
                    if enter_amount>accountdetails['acc_balance']:
                        print("You do not have this ammount of money!")
                    else:
                        new_balance=accountdetails['acc_balance']-enter_amount
                        data['people'][num]['acc_balance']=new_balance
                        with open('accounts.json','w') as f:
                            json.dump(data,f,indent=2)
                        print(f"Amount of Rs. {enter_amount} has been debited from your account!")
                        print(f"Your Balance is: {new_balance}")
                        sleep(3)
                        break

            elif choice2==4:
                new_num=0
                while True:
                    clear()
                    enter_acc_num=int(input("Enter the Account number of the account you want to transfer: "))
                    if enter_amount>accountdetails['acc_balance']:
                        print("You do not have this ammount of money!")
                    for i in range(len(data['people'])):
                        if enter_acc_num==data['people'][i]['acc_number']: 
                            new_num=i
                            break
                    if i ==len(data['people']) and enter_acc_num != data['people'][i-1]['acc_number']:
                        print("Invalid Account Number!!")
                    if enter_acc_num==data['people'][new_num]['acc_number']: 
                        newaccountdetails=data['people'][new_num]
                        new_name=newaccountdetails['name']
                        check_if_name_ok=input(f"Do you want to transfer to {new_name}? (Y/N)")
                        while True:
                            if check_if_name_ok == 'Y' or check_if_name_ok == 'y':
                                amount=int(input("Enter the amount that you want to transfer: "))
                                other_person_new_balance=newaccountdetails['acc_balance']+amount
                                own_new_balance=accountdetails['acc_balance']-amount
                                data['people'][num]['acc_balance']=own_new_balance
                                data['people'][new_num]['acc_balance']=other_person_new_balance
                                with open('accounts.json','w') as f:
                                    json.dump(data,f,indent=2)
                                print("Transfer Complete")
                                sleep(3)
                                break
                            elif check_if_name_ok == 'N' or check_if_name_ok == 'n':
                                break
                            else:
                                print("Invalid Input Enter 'Y' or 'N'")
                        break
            elif choice2==6:
                break

            elif choice2==5:
                while True:
                    clear()
                    name=accountdetails['name']
                    pin=accountdetails['PIN']
                    balance=accountdetails['acc_balance']
                    acc_num=accountdetails['acc_number']
                    print(f"Account Holder Name: {name}\nAccount Number: {acc_num}\nPIN: {pin}\nAccount Balance: {balance}\n")
                    choice3=int(input("\n\n1. Change PIN\n2. Go back to Account Menu\n3. Delete Account\n"))
                    if choice3 == 2:
                        break
                    elif choice3 == 1:
                        while True:
                            clear()
                            curr_PIN=int(input("Enter your Current PIN: "))
                            if curr_PIN == accountdetails['PIN']:
                                new_PIN=int(input("Enter your New PIN: "))
                                if new_PIN>999 and new_PIN<10000:
                                    data['people'][num]['PIN']=new_PIN
                                    with open('accounts.json','w') as f:
                                        json.dump(data,f,indent=2)
                                    print(f"PIN changed Sucessfully!\nYour new PIN is: {new_PIN}")
                                    sleep(3)    
                                    break
                                else:
                                    print("PIN must be 4 Digit and cannot start with 0!\n")
                            else:
                                print("Incorrect PIN!")
                    elif choice3==3:
                        confirm=input("Are you sure you want to delete your account!!(Y/N)? ")
                        if confirm=='Y' or confirm=='y':
                            while True:
                                check_PIN_1=int(input("Enter Your PIN : "))
                                if check_PIN_1==accountdetails['PIN']:
                                    check_PIN_2=int(input("Re-enter Your PIN : "))
                                    if check_PIN_2==check_PIN_1:
                                        data['people'].pop(num)
                                        with open('accounts.json','w') as f:
                                            json.dump(data,f,indent=2)
                                        print("Account Sucessfully Deleted! and your money is gone forever!!")
                                        sleep(3)
                                        break
                                    else:
                                        print("The PINs do not match!")
                                else:
                                    print("Incorrect PIN!")
                        break

    else:
        print("There are no accounts in this bank!")

def about():
	print('''\n==========ABOUT US==========
        This project has been created by Aman Khadka.
        It is a basic Python Project for my 1st Semester.''')

def developer_mode():
    print(data)
    sleep(10)

#main
while True:
    clear()
    print("Welcome to the Bank of TBC\n")
    choice1=int(input("1. Sign up\n2. Login\n3. About\n4. Exit\n"))
    if choice1==1:
        new_user()
    elif choice1==2:
        existing_user()
    elif choice1==3:
        about()
    elif choice1==5:
        developer_mode()
    elif choice1==4:
        break