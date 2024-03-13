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
    print(Fore.RESET + f"Hello {screen_name}! Below you can see the amount of currency you have\n"
                       f"and your distance to the aliens."
                       f"Don't let either of them run out or your mission will fail!\n")
    user_currency_distance(screen_name)
    input(Fore.BLUE + "\nTime to start the journey. Press enter to open check-in for your first flight.")

    # 1. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = suspicious_employee(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nThat was unexpected...and time consuming. Maybe it's better to hurry.\n"
                       f"Press enter to open check-in.")

    # 2. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = crazy_dice(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nWhat an interesting game! But now it's time to move on.\n"
                       f"Press enter to open check-in.")

    # 3. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = currency_converter(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nThat traveller was really weird?! let's go and see where you can go next.\n"
                       f"Press enter to open check-in.")

    # 4. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = country_capital(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nHow kind of you to help that child, but can you now focus on continuing the journey.\n"
                       f"Press enter to open check-in")

    # 5. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = hiding_closet(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nI wonder why that fugitive was on the run? Oh well, it's not our business,\n"
                       f"so time to move on. Press enter to open check-in.")

    # 6. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = flight_cancelled(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nFlight cancellations are always so unfortunate. But it is what it is so keep going.\n"
                       f"Press enter to open check-in.")

    # NORJA 7. maa ja tehtävä
    boolean_game_on = select_airport_norway(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = fahrenheit_to_celsius(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nThat almost gave me a heart attack! Fortunately you got the situation fixed\n"
                       f"and you can now start the journey back to Cuba. Press enter to open check-in.")

    # 8. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = run_or_hide(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.RESET + f"That was a big raid! I'm surprised you didn't get caught?!\n"
                       f"Maybe it's better to hurry and leave. Press enter to open check-in.\n")

    # 9. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = makeover_time(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nWhat a fun group that was! But now, carry on. Press enter to open check-in.")

    # 10. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = fake_chemist(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nNext time try not to panic and think before you open your mouth.\n"
                       f"Somehow you survived so let's go! Press enter to open check-in.")

    # 11. maa ja tehtävä
    boolean_game_on = select_airport(screen_name)
    if boolean_game_on == False:
        break
    boolean_game_on = resistance_test(screen_name)
    if boolean_game_on == False:
        break
    input(Fore.BLUE + f"\nWell, did you answer your new friend's question correctly? Actually I don't really care.\n"
                       f"Hurry up and keep going! Press enter to open check-in.")

    # 12. maa, takaisin Kuubaan
    select_airport_cuba(screen_name)
    break