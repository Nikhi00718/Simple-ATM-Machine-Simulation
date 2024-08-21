# Initial balance set to $500.
balance = 500  

# Start an infinite loop to keep the ATM operational until the user decides to exit.
while True:
    # Display the ATM menu with a clean and organized look.
    print("          WELCOME TO THE ATM          ")
    print()
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print()
    
    # Get the user's menu selection.
    choice = input("Please select an option (1-4): ")
    
    # Handle checking the balance.
    if choice == '1':
        print(f"\nYour current balance is: ${balance}")
        continue
    
    # Handle withdrawing money.
    elif choice == '2':
        amount = input("\nEnter the amount to withdraw: $")
        if amount.isdigit():  # Ensure the input is numeric.
            amount = int(amount)
            if amount > balance:
                print("\nInsufficient funds. Please enter an amount less than or equal to your balance.")
            else:
                balance -= amount
                print(f"\n${amount} has been withdrawn.")
                print(f"New balance: ${balance}")
        else:
            print("\nInvalid input. Please enter a valid numeric value.")
        continue
    
    # Handle depositing money.
    elif choice == '3':
        amount = input("\nEnter the amount to deposit: $")
        if amount.isdigit():  # Ensure the input is numeric.
            amount = int(amount)
            balance += amount
            print(f"\n${amount} has been deposited.")
            print(f"New balance: ${balance}")
        else:
            print("\nInvalid input. Please enter a valid numeric value.")
        continue
    
    # Handle exiting the program.
    elif choice == '4':
        print("\nThank you for using the ATM. Goodbye!")
        break
    
    # Handle invalid menu selection.
    else:
        print("\nInvalid option. Please select a valid choice (1-4).")
        continue
