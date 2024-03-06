# tänne esim arpomis hommelit liikkumisee yms
import random
import mysql.connector
from connection import connect
from colorama import Fore

def user_currency_distance(screen_name):
    sql = (f"SELECT currency, alien_distance FROM game WHERE screen_name = '{screen_name}';")
    cursor = connect.cursor()
    cursor.execute(sql)
    currency, distance = cursor.fetchall()
    print(Fore.YELLOW + f"Currency: {currency} $")
    print(Fore.LIGHTRED_EX + f"Distance: {distance} steps")

#funktio lentokentältä toiselle lentämiseen
def select_airport():
    #Yhdistetään tietokantaan
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country")
    cursor = connect.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.close()

    # Valitaan satunnaisesti kolme lentokenttää
    selected_airports = random.sample(airports, 3)

    #pelaajan check-in ja funktio antaa kolme satunnaisesti arvottua lentokenttää ja tulostaa nämä l
    print("welcome to check-in!")
    print("Choose from the following airports your next destination:")
    for i in range(len(selected_airports)):
        print(f"{i + 1}. {selected_airports[i][0]} in {selected_airports[i][1]}")

    #pelaaja valitsee arvotuista lentokentistä seuraavan kohteen
    while True:
        choice = input("select next airport. Enter number between (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                break
        print("error in selection. enter number between 1-3.")

    decided_airport = selected_airports[choice - 1][0]
    print(f"your choice as the next destination is: {decided_airport}")
    return decided_airport

#Testi
chosen_airport = select_airport()
print("have a safe flight to", chosen_airport + "!")

def currency_add(add_amount, screen_name):
    currency_sql = f"UPDATE game SET currency += '{add_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    reuslt = cursor.fetchall()

def currency_subtract(subtract_amount, screen_name):
    currency_sql = f"UPDATE game SET currency -= '{subtract_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    reuslt = cursor.fetchall()

def distance_add(add_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance += {add_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    reuslt = cursor.fetchall()

def distance_substract(subtract_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance += {subtract_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    reuslt = cursor.fetchall()