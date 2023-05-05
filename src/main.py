from user_functions import atm_user

print("\t***************************")
print("\t***  Welcome To CA ATM  ***")
print("\t***************************")

# print("Press enter to continue")
# acc_holder = acc_name()

# acc_name = ["Simon, Mary, John, Lily"]

# acc_id = ""

# while True:
#     try:
#         acc_id = input("What is your name?")
#         acc_found = [account for account in acc_name if acc_name == acc_id]
#         if(len(acc_found) > 0):
#             acc_holder = acc_found[0]
#             break
#         else:
#             print("Account not found")
#     except:
#         print("Account not found")

# def user_menu():
#     print ("Please choose an option:")
#     print ("1. Withdraw")
#     print ("2. Deposit")
#     print ("3. Check balance")
#     print ("4. Exit")

# password = 1111
user_choice = 0
balance = 5000

# pin = int(input("Enter your pin: "))

# if pin == password:

current_user = atm_user("","")

list_of_user = []

list_of_user.append(atm_user("simon","1234"))
list_of_user.append(atm_user("mary","1234"))

loginId = ""

while True:
    try:
        loginId = input(str("What is your log in ID?: "))
        Id_match = [id for id in list_of_user if id.userId == loginId]
        if(len(Id_match) > 0):
            current_user = Id_match
            break
        else:
            print("Incorrect User ID. Please try again")
    except:
        print("Incorrect User ID. Please try again")

while user_choice !=4:
    print ("Please choose an option:")
    print ("1. Withdraw")
    print ("2. Deposit")
    print ("3. Check balance")
    print ("4. Exit")
    try:
        user_choice = int(input("What would you like to do?: "))
    except:
        print ("invalid input")

    if user_choice == 1:
        withdraw = int(input("How much would you like to withdraw?: "))
        balance -= withdraw
        print ("withdraw amount:", withdraw)
        print ("Your remaining balance is: ", balance)
    
    elif user_choice == 2:
        deposit = int(input("How much would you like to deposit?: "))
        balance += deposit
        print ("Deposit amount:", deposit)
        print ("Your remaining balance is: ", balance)
    
    elif user_choice == 3:
        print (balance)

    elif user_choice == 4:
        print ("Goodbye, have a nice day.")

    elif user_choice >= 5:
        print ("invalid input")

# else:
#     print("Incorrect pin")