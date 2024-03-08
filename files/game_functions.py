# tänne esim arpomis hommelit liikkumisee yms
import random
import mysql.connector
from connection import connect
from colorama import Fore
from win_or_loose import you_win, game_over

def user_currency_distance(screen_name):
    sql = (f"SELECT currency, alien_distance FROM game WHERE screen_name = '{screen_name}';")
    cursor = connect.cursor()
    cursor.execute(sql)
    userdata = cursor.fetchall()
    for data in userdata:
        print(Fore.YELLOW + f"    Currency: {data[0]} $\n    Distance: {data[1]} steps")

#funktio lentokentältä toiselle lentämiseen
def select_airport(screen_name):
    #Yhdistetään tietokantaan
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name != 'Norway'")
    cursor = connect.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.close()

    # Valitaan satunnaisesti kolme lentokenttää
    selected_airports = random.sample(airports, 3)

    #pelaajan check-in ja funktio antaa kolme satunnaisesti arvottua lentokenttää ja tulostaa nämä l
    print(Fore.RESET + "\nWelcome to check-in!")
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

def select_airport_norway(screen_name):
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name = 'Norway'")
    cursor = connect.cursor()
    cursor.execute(sql)
    norway = cursor.fetchone()
    cursor.close()

    print(Fore.RESET + "Welcome to check-in!")
    print(f"Choose from the following airports your next destination:\n")
    print(f"1. {norway[0]} in {norway[1]}")
    input("Valitse lentokenttä: ")

    norway_airport = norway[0]
    sql2 = f"UPDATE game SET location = (SELECT ident FROM airport WHERE name = '{norway_airport}') WHERE screen_name = '{screen_name}';"
    cursor = connect.cursor()
    cursor.execute(sql2)
    location_change = cursor.fetchall()
    cursor.close()
    currency_subtract(10, screen_name)
    print(f"\nWelcome to {norway_airport}!\n")
    user_currency_distance(screen_name)

def select_airport_cuba(screen_name):
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name = 'Cuba'")
    cursor = connect.cursor()
    cursor.execute(sql)
    cuba = cursor.fetchone()
    cursor.close()

    print(Fore.RESET + "Welcome to check-in!")
    print(f"Choose from the following airports your next destination:\n")
    print(f"1. {cuba[0]} in {cuba[1]}")
    input("Valitse lentokenttä: ")

    cuba_airport = cuba[0]
    sql2 = f"UPDATE game SET location = (SELECT ident FROM airport WHERE name = '{cuba_airport}') WHERE screen_name = '{screen_name}';"
    cursor = connect.cursor()
    cursor.execute(sql2)
    location_change = cursor.fetchall()
    cursor.close()
    currency_subtract(10, screen_name)
    print(f"\nWelcome to {cuba_airport}!\n")
    user_currency_distance(screen_name)

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

def check_if_name_taken(screen_name):
    cursor = connect.cursor()
    name_sql = f"SELECT COUNT(*) FROM game WHERE screen_name='{screen_name}'" #lasketaan montako kertaa annettu nimi esiintyy game taulussa
    cursor.execute(name_sql)
    result = cursor.fetchone()[0] # ilman [0] tulostaa '(0,)', eli otetaan tuplen ensimmäinen numero
    print(result)
    if result > 0: #jos samoja nimiä enemmän ku 0 -> palauttaa False. Mainissa While loopissa palataan takas pelaajan nimen kysymiseen
        print('Username already taken. Try something else.')
        return False
    else: # kaikki ok ei oo samoja nimiä
        print('Username selected. Continue.')
        return True

def check_if_game_over(screen_name):
    cursor = connect.cursor()
    game_sql = f"SELECT location, currency, alien_distance, in_possession FROM game WHERE screen_name='{screen_name}';"
    cursor.execute(game_sql)
    result = cursor.fetchall()
    if result[0] == 'MUHA' and result[3] == 1:
        you_win()
    elif result[1] == 0:
        print("You ran out of money... :(")
        game_over()
        break
    elif result[2] == 0:
        print("The aliens got you brooo wtf?!!?")
        game_over()
        break
