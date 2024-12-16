Bank Management System

Overview

This project implements a Bank Management System in Python, offering core banking functionalities. The system has two variations:
1.Command-line Interface (CLI) implementation in bank_management.py.
2.Graphical User Interface (GUI) implementation using Streamlit in app.py.
Both implementations manage banking operations like account creation, deposits, withdrawals, balance inquiries, user updates, and account deletion.

Features

Common Features
-Account Creation: Create a new account with an account number, name, age, and initial balance.
-Account Validation: Verify whether an account exists.
-Deposit Money: Add money to an account.
-Withdraw Money: Withdraw money while ensuring a minimum balance is maintained.
-Balance Inquiry: Check the current balance of an account.
-Update User Details: Modify account holder’s name and age.
-Account Deletion: Permanently remove an account.

CLI (bank_management.py)
-Text-based menu-driven program.
-Interactive input through the terminal.
-Suitable for environments without GUI support.

GUI (app.py)
-Interactive web-based application using Streamlit.
-Sidebar menu for navigation.
-Easy-to-use graphical interface for performing banking operations.


File Descriptions

bank_management.py
-Implements a terminal-based Bank Management System.
-Uses file-based storage (accounts.txt) to store and retrieve account information.
-Runs as a standalone application.

app.py
-Streamlit-based GUI application for the Bank Management System.
-Provides an intuitive and modern web interface.
-Requires a browser to access the system.

accounts.txt
-Stores account information in the format:
 <account_number>,<name>,<age>,<balance>
-Used as a shared database for both the CLI and GUI versions.


Functional Workflow

Account Creation
-Inputs: Account number, name, age, initial balance.
-Process: Checks for account existence and writes details to accounts.txt.
-Outputs: Confirmation of account creation or error message.

Deposit and Withdrawal
-Inputs: Account number, amount.
-Process: Validates account existence and updates balance.
-Outputs: New balance or error message (e.g., insufficient funds).

Balance Inquiry
-Inputs: Account number.
-Outputs: Displays the current balance.

Update User Details
-Inputs: Account number, updated name, updated age.
-Outputs: Confirmation of update or error message.

Delete Account
-Inputs: Account number.
-Process: Removes the account entry from accounts.txt.
-Outputs: Confirmation of deletion.


















