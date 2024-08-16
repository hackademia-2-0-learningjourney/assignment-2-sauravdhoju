'''
WAP that first gives 2 options: 

    Sign up
    Sign in

when 1 is pressed user needs to provide following information 

    Username, 2. Password, 3. Mobile number

All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 

Do it using json files, save everything to json and load from json 

'''

import json
import os

def signIn(records):
    username = input('Username: ')
    password = input('Password: ')

    if os.path.exists(records):
        with open(records, 'r') as f:
            data = json.load(f)

        if username in data and data[username]['password'] == password:
            print('Sign in successful')
            print('--' * 25)
            print('Welcome to The device')
            print(f'Mobile Number: {data[username]["mobileNumber"]}')
        else:
            print('Incorrect credentials. Terminating the program.')
            exit()
    else:
        print('No user records found. Please sign up first')

def signUp(records):
    username = input('Username: ')
    password = input('Password: ')
    mobileNumber = input('Mobile Number: ')

    if os.path.exists(records):
        with open(records, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    if username in data:
        print(f'Username {username} is already taken!')
    else:
        data[username] = {
            'password': password,
            'mobileNumber': mobileNumber,
        }

        with open(records, 'w') as f:
            json.dump(data, f, indent=4)
        print('Sign Up successful')

def main():
    records = 'database.json'
    choice = int(input('1. Sign In \n2. Sign Up\nChoice: '))

    if choice == 1:
        signIn(records)
    elif choice == 2:
        signUp(records)
    else:
        print('Enter a valid number')

if __name__ == "__main__":
    main()
