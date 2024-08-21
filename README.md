# Simple-ATM-Machine-Simulation
This repository contains a Python program that simulates a basic ATM machine. The program allows users to perform common banking transactions such as checking their balance, withdrawing money, and depositing money. The ATM operates in a loop, continuously offering these options until the user decides to exit.
## Features:
Check Balance: Users can view their current account balance at any time.
Withdraw Money: Users can withdraw funds, with safeguards to ensure they don't withdraw more than their available balance.
Deposit Money: Users can deposit funds into their account, and the balance updates accordingly.
Exit: Users can exit the ATM system gracefully.
## How It Works:
Initial Setup: The program starts with a predefined balance of $500.
User Interaction: The ATM presents a menu with four options:
Check Balance
Withdraw Money
Deposit Money
Exit
Transaction Processing: Depending on the user's choice, the program:
Displays the balance.
Allows withdrawal if the entered amount is within the balance limit.
Allows deposit of a specified amount.
Ends the session when the user chooses to exit.
Looping: The ATM continues to operate in a loop, returning to the menu after each transaction until the user selects the exit option.
## Example Scenarios
Checking Balance: If the user selects the balance option, they see the current balance displayed on the screen.
Withdrawing Money: The user enters the amount they wish to withdraw. If it's within their available balance, the amount is deducted; otherwise, an error message is displayed.
Depositing Money: The user enters the amount to deposit, and their balance is updated accordingly.
Exiting: The program thanks the user and terminates when they choose to exit.
## Expected Errors
Invalid Input (Non-Numeric Values): If a user inputs non-numeric characters when prompted for a withdrawal or deposit amount, the program will display an "Invalid input" message and prompt the user to enter a valid numeric value.
Insufficient Funds: When attempting to withdraw more money than is available in the account, the program will display an "Insufficient funds" message and prevent the transaction.
Invalid Menu Option: If the user selects an option outside of the range 1-4, the program will notify them with an "Invalid option" message and prompt them to select a valid option.
## Code Structure
Input Handling: The program carefully checks user inputs to ensure they are valid numeric values before processing transactions.
Menu Navigation: The main loop presents the menu options and processes user choices.
Balance Management: The balance is updated based on deposits and withdrawals, with safeguards to prevent overdrafts.
Running the Program
To run the program, simply execute the Python script. The ATM interface will appear in the console, and you can interact with it by typing the corresponding numbers for each option.

## Future Enhancements
Multi-User Support: Extend the program to support multiple users with individual accounts.
Security Features: Implement PIN-based access for added security.
Transaction History: Add a feature to track and display the transaction history for each session.
