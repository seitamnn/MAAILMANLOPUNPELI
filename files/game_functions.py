# tänne esim arpomis hommelit liikkumisee yms
import random
import mysql.connector
from connection import connect
from colorama import Fore
from win_or_loose import you_win, game_over
import time
from help import help_command, help_center

# Funktio pelaajan tietojen tulostamiseen
def user_currency_distance(screen_name):
        sql = (f"SELECT currency, alien_distance FROM game WHERE screen_name = '{screen_name}'")
        cursor = connect.cursor()
        cursor.execute(sql)
        userdata = cursor.fetchall()
        for data in userdata:
            print(Fore.YELLOW + f"    Currency: {data[0]} $\n    Distance: {data[1]} steps")

#funktio lentokentältä toiselle lentämiseen
def select_airport(screen_name):
    while True:

        #Yhdistetään tietokantaan
        sql = f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name != 'Norway'"
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
            help_command(screen_name, choice)
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 3:
                    break
            print(Fore.RESET + "Error in selection. enter number between 1-3.")

        decided_airport = selected_airports[choice - 1][0]
        sql2 = f"UPDATE game SET location = (SELECT ident FROM airport WHERE name = '{decided_airport}') WHERE screen_name = '{screen_name}';"
        cursor = connect.cursor()
        cursor.execute(sql2)
        location_change = cursor.fetchall()
        cursor.close()
        currency_subtract(10, screen_name)
        print(Fore.GREEN + f"\nWelcome to {decided_airport}!\n")
        user_currency_distance(screen_name)
        return check_if_game_over(screen_name)

# Norja kenttään pääsemiseksi oma funktio
def select_airport_norway(screen_name):
    sql = f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name = 'Norway'"
    cursor = connect.cursor()
    cursor.execute(sql)
    norway = cursor.fetchone() # airport, country
    cursor.close()

    # Pelaajalle annetaan vaihtoehdoksi ainoastaan Norja
    print(Fore.RESET + "Welcome to check-in!")
    print(f"Oh look! There is a direct flight to Norway from here. The flight would also seem to be safe to do now\n")
    print(f"1. {norway[0]} in {norway[1]}")
    answer = input("Enter 1 to continue: ")
    help_command(screen_name, answer)


    norway_airport = norway[0]
    sql2 = f"UPDATE game SET in_possession = TRUE, location = (SELECT ident FROM airport WHERE name = '{norway_airport}') WHERE screen_name = '{screen_name}';"
    cursor = connect.cursor()
    cursor.execute(sql2)
    location_change = cursor.fetchall()
    cursor.close()
    currency_subtract(10, screen_name)
    print(Fore.GREEN + f"\nWelcome to {norway_airport}!\n")
    user_currency_distance(screen_name)
    return check_if_game_over(screen_name)

# Kuuba kentälle pääsemiseksi oma funktio
def select_airport_cuba(screen_name):
    sql = f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.name = 'Cuba'"
    cursor = connect.cursor()
    cursor.execute(sql)
    cuba = cursor.fetchone() # airport, country
    cursor.close()

    print(Fore.RESET + "Welcome to check-in!")
    print(f"Finally! There is a direct and safe flight to cuba from here! It's time for your last flight\n")
    print(f"1. {cuba[0]} in {cuba[1]}")
    input("Enter 1 to continue: ")

    cuba_airport = cuba[0]
    sql2 = f"UPDATE game SET location = (SELECT ident FROM airport WHERE name = '{cuba_airport}') WHERE screen_name = '{screen_name}';"
    cursor = connect.cursor()
    cursor.execute(sql2)
    location_change = cursor.fetchall()
    cursor.close()
    currency_subtract(10, screen_name)
    print(Fore.GREEN + f"\nWelcome to {cuba_airport}!\n")
    user_currency_distance(screen_name)
    return check_if_game_over(screen_name)

# Funktio valuutan lisäämiseksi
def currency_add(add_amount, screen_name):
    currency_sql = f"UPDATE game SET currency = currency + '{add_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    result = cursor.fetchall()

# Funktio valuutan vähentämiseksi
def currency_subtract(subtract_amount, screen_name):
    currency_sql = f"UPDATE game SET currency = currency - '{subtract_amount}' WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(currency_sql)
    result = cursor.fetchall()

# Funktio etäisyyden lisäämiseksi
def distance_add(add_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance + {add_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    result = cursor.fetchall()

# Funktio etäisyyden vähentämiseksi
def distance_substract(subtract_amount, screen_name):
    distance_sql = f"UPDATE game SET alien_distance = alien_distance - {subtract_amount} WHERE screen_name = '{screen_name}'"
    cursor = connect.cursor()
    cursor.execute(distance_sql)
    result = cursor.fetchall()

# Funktio, joka tarkastaa onko annettu nimi pelaajalle jo käytössä.
def check_if_name_taken(screen_name):
    cursor = connect.cursor()
    name_sql = f"SELECT COUNT(*) FROM game WHERE screen_name='{screen_name}'" #lasketaan montako kertaa annettu nimi esiintyy game taulussa
    cursor.execute(name_sql)
    result = cursor.fetchone()[0] # ilman [0] tulostaa '(0,)', eli otetaan tuplen ensimmäinen numero
    if result > 0: # jos samoja nimiä enemmän ku 0 -> palauttaa False. Mainissa While loopissa palataan takas pelaajan nimen kysymiseen
        print('Username already taken. Try something else.')
        return False
    else: # kaikki ok ei oo samoja nimiä
        print('Username selected. Continue.')
        return True

# Funktio, joka tarkastaa onko peli vielä käynnissä jokaisen mahdollisesti tietokannan dataa muokkaavan tilanteen kohdalle
def check_if_game_over(screen_name):
    #global game_on
    cursor = connect.cursor()
    game_sql = f"SELECT location, currency, alien_distance, in_possession FROM game WHERE screen_name='{screen_name}';"
    cursor.execute(game_sql)
    result = cursor.fetchall()
    if result[0][0] == 'MUHA': # jos sijainti on takas Kuubas ja ainesosa pelaajan hallussa
        you_win()
        win_end_text = (Fore.GREEN + f'''
    As you step into the resistance laboratory in Cuba, carrying the ancient ingredient
    that holds the key to humanity's survival, a wave of relief washes over you.
    The journey has been long and exhausting, and dangerous situations were not avoided,
    but you overcame all adversity.
    The antidote can now be made, thanks to your bravery and determination.\n
    As the scientists begin their work, you take a moment to reflect on the magnitude of what 
    you've accomplished. Against the backdrop of an alien invasion and the looming threat of 
    annihilation, you have stood firm, a beacon of hope in humanity's darkest hour.\n
    Word of your success spreads quickly, igniting a spark of hope in the hearts of people
    around the world. With the understanding that they're now closer to winning,
    the resistance becomes even stronger and more determined.\n
    But the fight is far from over. The aliens still pose a formidable threat, and the struggle
    for survival continues. Yet, as long as there are those willing to stand up and fight,
    humanity will never surrender.\n
    You may have won this battle, but the war rages on. And as long as there are heroes like you,
    humanity will endure, resilient and unyielding in the face of any challenge that may come its way.''')
        for letter in win_end_text:
            print(letter, end='',
                  flush=True)
            time.sleep(0.03)
        print()
        return False
    elif result[0][1] == 0: # jos currency on nollissa
        game_over()
        game_over_currency = Fore.RED + f'''
    You ran out of currency! Now you are stuck at the current airport and can't move forward.
    Because you got stuck, no antidote could be made on time and the aliens were able to 
    spread their virus and wipe out all living things from the face of the earth.'''
        for letter in game_over_currency:
            print(letter, end='',
                  flush=True)
            time.sleep(0.03)
        print()
        return False
    elif result[0][2] == 0: # jos etäisyys alieneista nollassa
        game_over()
        game_over_distance = Fore.RED + f'''
    The aliens caught you! And you are now their prisoner. Because you got caught,
    no antidote could be made on time and the aliens were able to spread their virus
    and wipe out all living things from the face of the earth.'''
        for letter in game_over_distance:
            print(letter, end='',
                  flush=True)
            time.sleep(0.03)
        print()
        return False
    else:
        return True


def check_if_game_over_fahrenheit(screen_name):
        cursor = connect.cursor()
        game_sql = f"SELECT location, currency, alien_distance, in_possession FROM game WHERE screen_name='{screen_name}';"
        cursor.execute(game_sql)
        result = cursor.fetchall()
        if result[0][2] == 0:  # jos etäisyys alieneista nollassa

            return False
        else:
            return True
