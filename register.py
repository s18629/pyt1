import csv
import getpass


def register_new_user():
    username = '_'
    while not username.isalnum():
        username = input("Enter username ")

    password = '_'
    while not password.isalnum():
        password = input("Enter password ")

    save_new_user_in_db(username, password)


def save_new_user_in_db(username, password):
    with open('db.csv', 'a+', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': username, 'password': password})


def username_existing_checker(username, password):
    with open('db.csv') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            # print(line[0])
            if username in line[0]:
                print("username is unavailable")
                pass
        save_new_user_in_db(username, password)


def show_all_users():
    with open('db.csv') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print(line[0])
