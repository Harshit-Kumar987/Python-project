correct_id = "user"
correct_password = "1234"
attempts = 3
while attempts > 0:
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    if user_id == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("attempts remaining: ",attempts)
            print("Invalid ID or Password. Try again.")
        else:
            print("Account Locked")
