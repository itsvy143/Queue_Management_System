# Queue Management System
# Initial Project Setup

print("========================")
print("Queue Management System")
print("========================")

print("Welcome!")

customer_name = input("Enter your name: ")
customer_program = input("Enter your program and section: ")
customer_purpose = input("Enter your purpose: ")

queue_number = 1

print("====CUSTOMER INFORMATION====")
print("Customer:", customer_name)
print("Program & Scetion:", customer_program)
print("Purpose:", customer_purpose)
print("============================")
print("Your queue number is:", queue_number)

print("Please select an option.")

number = 1

while number <= 5: 
    print("Queue Number:", number)
    number = number + 2

    print()
    print("====MENU====")
    print("1. Get Queue Number")
    print("2. View Queue")
    print("3. Serve Next Customer")
    print("4. About the System")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Get Queue Number.")

    elif  choice == "2":
        print("You selected View Queue.")

    elif choice == "3":
        print("You selected Serve Next Customer.")

    elif choice == "4":
        print("You selected About the System.")

    elif choice == "5":
        print("Thank you for using the Queue Management System.")
        break

    else:
        print("Invalid choice.")


print("Please wait for your turn.")