import connection

start = input("Would you like to start? (Y/N) \n").lower()
if start == 'y':
    print("Welcome to our game!")
    cursor = connection.connect