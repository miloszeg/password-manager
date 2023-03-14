from password_manager import PasswordManager

# Create a new PasswordManager instance
pm = PasswordManager()

# Display the main menu
print("Welcome to the Password Manager!")
print("1. Add a new password")
print("2. View saved passwords")
print("3. Delete a password")
print("4. Quit")

# Get user input and perform the corresponding action
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        pm.add_password()
    elif choice == "2":
        pm.view_passwords()
    elif choice == "3":
        pm.delete_password()
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")
