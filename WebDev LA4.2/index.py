# Registration storage
user_info = {}

# Registration
print("=== User Registration ===")
user_info['first_name'] = input("Enter First Name: ")
user_info['last_name'] = input("Enter Last Name: ")
user_info['course'] = input("Enter Course: ")
user_info['year_level'] = input("Enter Year Level: ")
user_info['section'] = input("Enter Section: ")
user_info['username'] = input("Create Username: ")
user_info['password'] = input("Create Password: ")

# Validate PIN Code length
while True:
    pin = input("Create Pin Code (Max 8 digits): ")
    if len(pin) <= 8 and pin.isdigit():
        user_info['pincode'] = pin
        break
    else:
        print("Pin must be numeric and up to 8 digits only. Try again.")

# Congratulate the user
print(f"\n Congratulations {user_info['first_name']}! You have successfully registered.\n")

# Ask to login 
login_choice = input("Do you want to log in now? (yes/no): ").lower()

if login_choice == "yes":
    # Loop for username/password authentication
    while True:
        username_input = input("Enter Username: ")
        password_input = input("Enter Password: ")

        if username_input == user_info['username'] and password_input == user_info['password']:
            print("Username and Password verified.")
            break
        else:
            print("Incorrect Username or Password. Try again.")

    # Loop for pin code authentication
    while True:
        pin_input = input("Enter your Pin Code: ")
        if pin_input == user_info['pincode']:
            print("\n Access Granted! Here are your registered details:\n")
            for key, value in user_info.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            break
        else:
            print("Incorrect Pin Code. Try again.")
else:
    print("Exiting the program. Goodbye!")
