from user_functions import atm_user
import csv

print("\t***************************")
print("\t***  Welcome To CA ATM  ***")
print("\t***************************")

user_choice = 0
balance = 5000
current_user = atm_user("","")

list_of_user = []

list_of_user.append(atm_user("simon", 1234))
list_of_user.append(atm_user("mary", 1234))

loginId = ""

file_name = "login.csv"

try:
    login_file = open(file_name, "r")
    login_file.close()
    print("Please Log in using the following ID and PIN:")

except FileNotFoundError as e:
    login_file = open(file_name, "w")
    login_file.write("ID,PIN,BALANCE\n")
    login_file.write("simon,1234,10000.50\n")
    login_file.write("mary,4321,5000.23\n")
    login_file.close()
    print("Account has been registered")

with open(file_name, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0], row[1])

while True:
    try:
        loginId = str(input("Please enter your log in ID: \n").strip().lower())
        Id_match = [id for id in list_of_user if id.userId == loginId]
        if(len(Id_match) > 0):
            current_user = Id_match[0]
            break
        else:
            print("Incorrect User ID. Please try again")
    except:
        print("Incorrect User ID. Please try again")

while True:
    try:
        pin = int(input("Please enter your pin: \n").strip())
        if(current_user.get_userPin() == pin):
            break
        else:
            print("Incorrect PIN. Please try again.")
    except:
        print("Incorrect PIN. Please try again.")

# print("Welcome", ) add names to class tomorrow.

while user_choice !=4:
    print ("\nPlease choose an option:\n")
    print ("1. Withdraw")
    print ("2. Deposit")
    print ("3. Check balance")
    print ("4. Exit")
    try:
        user_choice = int(input("\nWhat would you like to do?: \n"))
    except:
        print ("invalid input")

    if user_choice == 1:
        try:
            withdraw = float(input("How much would you like to withdraw?: \n"))
            if(balance < withdraw):
                print("Insufficient funds. Please try again\n")
            else:
                balance -= withdraw
                print ("withdraw amount: \n", withdraw,"\n")
                print ("Your remaining balance is: \n", balance)
        except:
            print("Invalid input. Please try again\n")
    
    elif user_choice == 2:
        deposit = float(input("How much would you like to deposit?: \n"))
        balance += deposit
        print ("\nDeposit amount: \n", deposit,"\n")
        print ("Your remaining balance is: \n", balance)
    
    elif user_choice == 3:
        print (balance)

    elif user_choice == 4:
        print ("\nGoodbye, have a nice day.")

    elif user_choice >= 5:
        print ("invalid input")