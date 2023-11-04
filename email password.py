email=input("Enter your Email:")


if '@' in email:
    password=input("Enter your password:")
    if email == "Dushii@gmail.com" and password == "1234":
        print("Welcome to Dushii World")
    elif email== "Dushii@gmail.com" and password != "1234":
        print("Password Incorrect")
        password=input("Please re enter password")
        if password=="1234":
            print("Finally correct")
        else:
            print("still incorrect")
    else:
        print("Invalid credentials")
else:
    print("Email is wrong:")