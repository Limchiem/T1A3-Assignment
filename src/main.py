from user_functions import atm_user

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

while True:
    try:
        loginId = str(input("Please enter your log in ID: ").strip().lower())
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
        pin = int(input("Please enter your pin: ").strip())
        if(current_user.get_userPin() == pin):
            break
        else:
            print("Incorrect PIN. Please try again.")
    except:
        print("Incorrect PIN. Please try again.")

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