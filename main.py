import register

if __name__ == '__main__':
    print("What do you want to do?")
    print("1. Register")
    print("2. Login")
    user_choice = input("").upper()

    if user_choice == "REGISTER" or "1":
        register.register_new_user()
