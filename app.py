import streamlit as st
import os

def account_exists(account_number):
    if not os.path.exists("accounts.txt"):
        return False
    with open("accounts.txt", "r") as file:
        for line in file:
            if line.startswith(account_number + ","):
                return True
    return False

def create_account(account_number, name, age, initial_balance):
    if account_exists(account_number):
        return "Account already exists!"
    
    with open("accounts.txt", "a") as file:
        file.write(f"{account_number},{name},{age},{initial_balance}\n")
    return "Account created successfully!"

def deposit_money(account_number, amount):
    if not account_exists(account_number):
        return "Account does not exist!"
    
    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                details[3] = str(float(details[3]) + amount)
            updated_lines.append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    return "Deposit successful!"

def withdraw_money(account_number, amount):
    if not account_exists(account_number):
        return "Account does not exist!"
    
    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                current_balance = float(details[3])
                if current_balance >= amount:
                    details[3] = str(current_balance - amount)
                else:
                    return "Insufficient balance!"
            updated_lines.append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    return "Withdrawal successful!"

# Streamlit Integration


def balance_inquiry(account_number):
    if not account_exists(account_number):
        return "Account does not exist!"
    
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                return f"Current Balance: {details[3]}"
    return "Account not found."

def update_user_details(account_number, name, age):
    if not account_exists(account_number):
        return "Account does not exist!"
    
    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] == account_number:
                details[1] = name
                details[2] = age
            updated_lines. append(",".join(details))

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    return "User  details updated successfully!"

def delete_account(account_number):
    if not account_exists(account_number):
        return "Account does not exist!"
    
    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            details = line.strip().split(",")
            if details[0] != account_number:
                updated_lines.append(line.strip())

    with open("accounts.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    return "Account deleted successfully!"


# Streamlit UI
st.title("Bank Management System")

menu = ["Create Account", "Deposit Money", "Withdraw Money" , "Balance Inquiry" , "Update User Details" , "Delete Account"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Create Account":
    st.subheader("Create a New Account")
    account_number = st.text_input("Account Number")
    name = st.text_input("Name")
    age = st.text_input("Age")
    initial_balance = st.number_input("Initial Balance", min_value=0.0)
    
    if st.button("Create Account"):
        result = create_account(account_number, name, age, initial_balance)
        st.success(result)

elif choice == "Deposit Money":
    st.subheader("Deposit Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Amount to Deposit", min_value=0.0)
    
    if st.button("Deposit"):
        result = deposit_money(account_number, amount)
        st.success(result)

elif choice == "Balance Inquiry":
    st.subheader("Check Balance")
    account_number = st.text_input("Account Number")
    
    if st.button("Check Balance"):
        result = balance_inquiry(account_number)
        st.success(result)

elif choice == "Withdraw Money":
    st.subheader("Withdraw Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Amount to Withdraw", min_value=0.0)
    
    if st.button("Withdraw"):
        result = withdraw_money(account_number, amount)
        st.success(result)

elif choice == "Update User Details":
    st.subheader("Update User Details")
    account_number = st.text_input("Account Number")
    name = st.text_input("New Name")
    age = st.text_input("New Age")
    
    if st.button("Update Details"):
        result = update_user_details(account_number, name, age)
        st.success(result)

elif choice == "Delete Account":
    st.subheader("Delete Account")
    account_number = st.text_input("Account Number")
    
    if st.button("Delete Account"):
        result = delete_account(account_number)
        st.success(result)
