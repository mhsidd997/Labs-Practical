def PasswordCheck(x):
    known_password = "ABC$123"
    if x.lower() == known_password.lower():
        print("Welcome!")
    else:
        print("I don't know you.")

# taking input from user
username = input("Enter your username: ")
password = input("Enter your password: ")

PasswordCheck(password)