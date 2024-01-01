def login_simulation():

    username = ""
    

    while username != "narengi":
        username = input("Enter your username: ")
        if username != "narengi":
            print("Incorrect username. Please try again.")

    password = ""
    
    
    while password != "1234":
        password = input("Enter your password: ")
        if password != "1234":
            print("Incorrect password. Please try again.")

    
    print("You've logged in successfully!")


login_simulation()