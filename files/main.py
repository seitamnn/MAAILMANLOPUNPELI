# Pääohjelma tähän lol
import connection
from connection import connect
import mysql.connector
from colorama import Fore
import time
import random
from start import start
from countryinfo import CountryInfo
from win_or_loose import game_over, you_win
from game_functions import user_currency_distance, distance_substract, currency_add, currency_subtract, select_airport
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

    screen_name = str(input("Select a player name: \n"))

    start(screen_name) # start-funktio luotu start-tiedostossa
    print(Fore.RESET + f"Haista paska {screen_name} tässä nää sun tietos idiootti\n")
    user_currency_distance(screen_name) # tulostetaan käyttäjälle tieot
    select_airport(screen_name)
    suspicious_employee(screen_name)
    hiding_closet(screen_name)
    resistance_test(screen_name)

