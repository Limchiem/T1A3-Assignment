import csv

# print("\t***************************")
# print("\t***  Welcome To CA ATM  ***")
# print("\t***************************")

# name of csv
file_name = "login.csv"

# run to check if csv file exist if not then it create with preloaded header login, pin, balance and prints out db created
# if csv file exist it prints out db exist
def welcome():
    try:
        db = open(file_name, "r")
        db.close()
        print("db exist")
    except FileNotFoundError as e:
        db = open(file_name, "w")
        db.write("login, PIN, Balance\n")
        db.close()
        print("db created")

# input user, pin, balance gets written to csv file
# accepts str, int and float for inputs
# checks if input is valid without crashing the app using try and except
def create_login(file_name):
    while True:
        try:
            user = input("Enter new Username: ")
            pin = int(input("Enter new Pin "))
            balance = float(input("Enter new balance: "))
            with open(file_name, "a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([user, pin, balance])
                break
        except:
            print("Something went wrong.")

# checks if log in details entered here matches created_login
# for loops used to check through each row for a match of user and pin
def login(file_name):
    while True:
        try:
            user = input("Enter Username: ")
            pin = int(input("Enter PIN: "))
            with open(file_name, "r", newline="") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    if row[0] == user and int(row[1]) == pin:
                        print("Login successful!")
                        return True, float(row[2])
                print("Invalid username or pin. Please try again.")
        except:
            print("Something went wrong.")

# main menu
def create_menu():
    print("\t***************************")
    print("\t***  Welcome To CA ATM  ***")
    print("\t***************************")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = input("Enter your selection: ")
    return choice

# balance function for main menu check csv file and matches user and balance
def get_balance(username):
    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == username:
                return float(row[2])
    print("Invalid user.")
    return None

# update balance function is used to when changes are made to get_balance by either withdraw or deposit function below
def update_balance(username, new_balance):
    rows = []
    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == username:
                row[2] = str(new_balance)
            rows.append(row)

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(rows)

# withdraw - current balance and display new balance
# doesn't allow you to withdraw funds that exceed your balance
def withdraw(username, amount):
    balance = get_balance(username)
    if balance is not None:
        if balance >= amount:
            new_balance = balance - amount
            update_balance(username, new_balance)
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid user")
# Deposit funds
def deposit(username, amount):
    balance = get_balance(username)
    if balance is not None:
        new_balance = balance + amount
        update_balance(username, new_balance)
        print(f"Deposit of {amount} successful.")
    else:
        print("Invalid user")

welcome()
create_login(file_name)
login(file_name)

choice = ""

while choice != "4":
    choice = create_menu()

    if choice == "1":
        username = input("Enter your username: ")
        balance = get_balance(username)
        if balance is not None:
            print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(username, amount)
    elif choice == "3":
        amount = float(input("Enter Deposit amount: "))
        deposit(username, amount)
    elif choice == "4":
        print("Thank you, and have a nice day.")
        break
    else:
        print("Invalid selection. Please try again.")