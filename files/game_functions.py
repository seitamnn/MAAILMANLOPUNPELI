# tänne esim arpomis hommelit liikkumisee yms
import random
import mysql.connector
from connection import connect
from colorama import Fore

def user_currency_distance(screen_name):
    sql = (f"SELECT currency, alien_distance FROM game WHERE screen_name = '{screen_name}';")
    cursor = connect.cursor()
    cursor.execute(sql)
    userdata = cursor.fetchall()
    for data in userdata:
        print(Fore.YELLOW + f"    Currency: {data[0]} $\n    Distance: {data[1]} steps\n")

#funktio lentokentältä toiselle lentämiseen
def select_airport(screen_name):
    #Yhdistetään tietokantaan
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country")
    cursor = connect.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.close()

    # Valitaan satunnaisesti kolme lentokenttää
    selected_airports = random.sample(airports, 3)

    #pelaajan check-in ja funktio antaa kolme satunnaisesti arvottua lentokenttää ja tulostaa nämä l
    print(Fore.RESET + "Welcome to check-in!")
    print("Choose from the following airports your next destination:\n")
    for i in range(len(selected_airports)):
        print(f"{i + 1}. {selected_airports[i][0]} in {selected_airports[i][1]}")

    #pelaaja valitsee arvotuista lentokentistä seuraavan kohteen
    while True:
        choice = input("\nSelect next airport. Enter number between (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                break
        print("Error in selection. enter number between 1-3.")

    decided_airport = selected_airports[choice - 1][0]
    sql2 = f"UPDATE game SET location = (SELECT ident FROM airport WHERE name = '{decided_airport}') WHERE screen_name = '{screen_name}';"
    cursor = connect.cursor()
    cursor.execute(sql2)
    location_change = cursor.fetchall()
    cursor.close()
    currency_subtract(10, screen_name)
    print(f"\nWelcome to {decided_airport}!\n")
    user_currency_distance(screen_name)

    return decided_airport

#Testi
#chosen_airport = select_airport()
#print("have a safe flight to", chosen_airport + "!")

def currency_add(add_amount, screen_name):
    currency_sql = f"UPDATE game SET currency = currency + '{add_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    result = cursor.fetchall()

def currency_subtract(subtract_amount, screen_name):
    currency_sql = f"UPDATE game SET currency = currency - '{subtract_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    result = cursor.fetchall()

def distance_add(add_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance + {add_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    result = cursor.fetchall()

def distance_substract(subtract_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance - {subtract_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    result = cursor.fetchall()