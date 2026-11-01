
# Menu Driven Banking Chatbot

print("Welcome to ABC Bank Chatbot!")

while True:

    print("\n--- Banking Services ---")
    print("1. Account Services")
    print("2. Balance Enquiry")
    print("3. Money Transfer")
    print("4. Loan Services")
    print("5. Customer Support")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n1. Open New Account")
        print("2. Update Account Details")

        sub = input("Enter sub-option: ")

        if sub == "1":
            print("You can open a new account by visiting the bank.")
        elif sub == "2":
            print("You can update your details at the bank.")
        else:
            print("Invalid sub-option!")

    elif choice == "2":
        print("Your account balance is Rs. 10,000")

    elif choice == "3":
        print("\n1. Transfer Money")
        print("2. Transfer Status")

        sub = input("Enter sub-option: ")

        if sub == "1":
            amount = input("Enter amount to transfer: ")
            print("Rs.", amount, "transfer request submitted.")

        elif sub == "2":
            print("Your last transaction is successful.")

        else:
            print("Invalid sub-option!")

    elif choice == "4":
        print("\n1. Personal Loan")
        print("2. Home Loan")

        sub = input("Enter sub-option: ")

        if sub == "1":
            print("Personal loan interest starts from 10%.")
        elif sub == "2":
            print("Home loan interest starts from 8%.")
        else:
            print("Invalid sub-option!")

    elif choice == "5":
        print("Contact customer support at 1800-123-456.")

    elif choice == "6":
        print("Thank you for using ABC Bank Chatbot!")
        break

    else:
        print("Invalid choice! Please select again.")
