def view_passwords():
    try:
        with open('password_manager.txt', 'r') as pwdmngr:      # Display stored usernames and passwords in 'password_manager.txt' file
            for line in pwdmngr.readlines():
                print(line.rstrip())
    except FileNotFoundError:
        print("Make sure the file exists before you try to view it!")


def add_passwords():
    user_name = input("Enter user name: ")
    password = input("Enter the password: ")
    site = input("Enter the program, app, or website this is being stored for: ")

    with open('password_manager.txt', 'a') as pwdmngr:
        pwdmngr.write(site + "\t" + "Username: " + user_name + "\t" + "Password: " + password + "\n")      # Add the user name and password to add to 'password_manager.txt'


while True:
    mode = input("Type 'view' to view passwords, 'add' to add a new password or 'e' to exit: ").lower()
    if mode == "e":
        break
    elif mode == "view":
        view_passwords()
    elif mode == "add":
        add_passwords()
    else:
        print("Invalid command entered. Please try again.")
        continue