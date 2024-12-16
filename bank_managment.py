import os

def create_account():
    account_number = input("Enter Account Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    initial_balance = float(input("Enter Initial Balance: "))

    if account_exists(account_number):
        print("Account already exists!")
        return

    with open("accounts.txt", "a") as file:
        file.write(f"{account_number},{name},{age},{initial_balance}\n")
    print("Account created successfully!")

def account_exists(account_number):
    if not os.path.exists("accounts.txt"):
        return False
    with open("accounts.txt", "r") as file:
        for line in file:
            if line.startswith(account_number + ","):
                return True
    return False

def deposit_money():
    account_number = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))

    if not account_exists(account_number):
        print("Account does not exist!")
        return

    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                details[3] = str(float(details[3]) + amount)
                print(f"New Balance: {details[3]}")
            updated_lines.append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    print("Deposit successful!")

def withdraw_money():
    account_number = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Withdraw: "))

    if not account_exists(account_number):
        print("Account does not exist!")
        return

    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                current_balance = float(details[3])
                if current_balance - amount < 1000:
                    print("Withdrawal denied! Balance cannot fall below ₹1000.")
                    return
                details[3] = str(current_balance - amount)
                print(f"New Balance: {details[3]}")
            updated_lines.append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    print("Withdrawal successful!")

def balance_inquiry():
    account_number = input("Enter Account Number: ")

    if not account_exists(account_number):
        print("Account does not exist!")
        return

    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                print(f"Current Balance: {details[3]}")
                return

def update_user_details():
    account_number = input("Enter Account Number: ")

    if not account_exists(account_number):
        print("Account does not exist!")
        return

    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                print(f"Current Details: Name: {details[1]}, Age: {details[2]}, Balance: {details[3]}")
                new_name = input("Enter new Name (leave blank to keep current): ")
                new_age = input("Enter new Age (leave blank to keep current): ")
                if new_name:
                    details[1] = new_name
                if new_age:
                    details[2] = new_age
            updated_lines.append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    print("User   details updated successfully!")

def delete_account():
    account_number = input("Enter Account Number to Delete: ")

    if not account_exists(account_number):
        print("Account does not exist!")
        return

    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] != account_number:
                updated_lines.append(line.strip())

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    print("Account deleted successfully!")

def main():
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Balance Inquiry")
        print("5. Update User Details")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            balance_inquiry()
        elif choice == '5':
            update_user_details()
        elif choice == '6':
            delete_account()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()