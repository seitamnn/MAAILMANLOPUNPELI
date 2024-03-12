import connection
from connection import connect
import mysql.connector
from colorama import Fore
import time
import random
from start import start
from countryinfo import CountryInfo
from win_or_loose import game_over, you_win
from game_functions import user_currency_distance, distance_substract, currency_add, currency_subtract, select_airport, select_airport_norway, select_airport_cuba, check_if_name_taken, check_if_game_over
from challenges import crazy_dice, currency_converter, recognized, fake_chemist, run_or_hide, flight_cancelled, fahrenheit_to_celsius, country_capital, suspicious_employee, makeover_time, hiding_closet, resistance_test

while True:
    print(Fore.RED + '''
    ██████╗     ███████╗     █████╗      ██████╗ 
    ╚════██╗    ██╔════╝    ██╔══██╗    ██╔════╝ 
     █████╔╝    ███████╗    ╚█████╔╝    ███████╗ 
    ██╔═══╝     ╚════██║    ██╔══██╗    ██╔═══██╗
    ███████╗    ███████║    ╚█████╔╝    ╚██████╔╝
    ╚══════╝    ╚══════╝     ╚════╝      ╚═════╝ 
    ''')

    start_choice = input("Would you like to start? (Y/N) \n").lower()
    if start_choice == 'y':
        print(Fore.RESET + "Welcome to our game!")
        cursor = connection.connect
    else:
        print("GAME OVER")
        game_over()
        break

    while True:
        screen_name = str(input("Select a player name: \n"))
        if check_if_name_taken(screen_name):
            break

    # Pelin aloitus
    start(screen_name) # start-funktio luotu start-tiedostossa
    print(Fore.RESET + f"Haista paska {screen_name} tässä nää sun tietos idiootti\n")
    user_currency_distance(screen_name)

    # 1. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = suspicious_employee(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 2. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = crazy_dice(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 3. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = currency_converter(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 4. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = country_capital(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 5. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = hiding_closet(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 6. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = flight_cancelled(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # NORJA 7. maa ja tehtävä
    boolean_game_on = select_airport_norway(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = fahrenheit_to_celsius(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 8. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = run_or_hide(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 9. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = makeover_time(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 10. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = fake_chemist(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 11. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    boolean_game_on = resistance_test(screen_name)
    print(boolean_game_on)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"\nSuoritit tehtävän. Nyt voit jatkaa matkaa seuraavalle kentälle.")

    # 12. maa, takaisin Kuubaan
    select_airport_cuba(screen_name)
    break