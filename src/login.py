def signup():
    
    username = input("Please type in a username: ").lower()
    password = input("Please type in a password: ").lower()

    confirm_pass = input("Please confirm password: ").lower()

    password_check = True
    while password_check:
        if confirm_pass == password:
            password_check == False
        else:
            confirm_pass =input("Passwords do not match, please confirm password: ")
    user_information = open("users.txt", "a")
    user_information.write(username + "," + password)
    user_information.close()


def login(x,y):
    verification = x + ',' + y
    if verification in "users.txt":
        return True
    else:
        return False


def main():
    user_confirmation = input("Do you already have an account? Y/N ").lower()
    if user_confirmation == 'y':
        counter = 0
        while counter < 4:
            username = input('Please type in your username: ').lower()
            password = input("Please type in your password: ").lower()
            
            if login(username,password) == True:
                print("Success! You're logged in.")
                break
            else:
                print("Incorrect login details try again.")
                counter += 1

    


if __name__ == "__main__":
    main()
    
