import mysql.connector
from connection import connect
from game_functions import check_if_game_over_fahrenheit, distance_add, distance_substract, currency_add, currency_subtract, check_if_game_over, user_currency_distance
import random
from countryinfo import CountryInfo
from colorama import Fore
import time

def currency_converter(screen_name): # tehtävä valuutan vaihto
    print(Fore.BLUE + f'''
    You are in your own thoughts when accidentally bump into strange looking world traveler at the airport. 
    He asks for your help with the currency conversion and you decide to help him. 
    Let's see what kind of problem he has.
    ''')

    answer = int(input(Fore. RESET + "How much is 10 euros in yens? "))
    if answer == 1630: # jos käyttäjän vastaus vastaa oikeaa vastausta
        print(Fore.GREEN + "That's right! The traveler is very grateful and gives you some currency\n"
                           "for the effort. You got 10$, hooray!")
        currency_add(10, screen_name) # lisätään valuuttaan 10
    else:
        print(Fore.RED + "That's not not quite right...")
        print(Fore. RED + "Oh no, the traveler fooled you. He was thief who took some currency from your pocket.\n"
                          "By chance he didn't get your wallet though. You lost 20$")
        currency_subtract(20, screen_name) # vähennetään valuuttaa -20
    return check_if_game_over(screen_name)


def recognized(screen_name): # tehtävä sinut tunnistetaan
    print(Fore.BLUE + f'''
    At the airport check-in one of the employees recognizes you. He looks at you disapprovingly. 
    You notice a pin on his chest. where it says 'END TO PLANET EARTH' He probably recognizes you from the news...
    because of the mission you've been on it a lot lately. What should you do about it?
    ''')

    answer = int(input(Fore.RESET + "You can either 1. try to bribe him or 2. "
                       "Ignore the situation as if nothing had happened. Now Choose (1/2) "))
    while True:
        if answer == 1: # jos lahjoo
            currency_subtract(10, screen_name)
            print(Fore.RED + "The bribes was useful and helps you keep a low profile."
                         "But now your wallet is a little bit lighter. You lose 10$")
            break
        elif answer == 2:
            distance_substract(1, screen_name)
            print(Fore.RED + "You tried to ignore the situation completely.\nThe employee lets "
                         "their anti-earth friends know about your location.\n Aliens are 1 step closer")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "I believe that was not one of the options I gave you...")
    return check_if_game_over(screen_name)


def fake_chemist(screen_name): # tehtävä huijaa olevasi kemisti
    print(Fore.BLUE + f'''
    At the airport security check, the metal part of the ingredient container causes problems.
    Container arouses the interest of employees and they start asking you questions about it.
    You panic, and decide to lie and explain that you're a chemist and that's why you have the 
    container with you. The employees don't fully believe you and they decide to test you. 
    ''')

    mycursor = connect.cursor() # osotetaa tietokantaa
    Fe = str(input(Fore.RESET + "What is the chemical symbol of iron? ")).lower() # eka testin kysymys
    if Fe == 'fe':
        print(Fore.GREEN + f"Your answer: '{Fe}' is correct!")
    else:
        currency_subtract(10, screen_name)
        distance_substract(1, screen_name)
        print(Fore.RED + "Your credibility begins to diminish. Carefully now!\n"
                         "This is taking too much time! Aliens are 1 distance step closer now!")
    Au = str(input(Fore.RESET + "What is the chemical symbol of gold? ")).lower() # toka testin kysymys
    if Au == 'au':
        print(Fore.GREEN + f"Your answer: '{Au}' is correct!")
    else:
        currency_subtract(10, screen_name)
        distance_substract(1, screen_name)
        print(Fore.RED + "Your credibility has almost entirely vanished. There's no room or time for errors now!\n"
                         "Aliens are yet another 1 distance step closer!")
    N = str(input(Fore.RESET + "What is the chemical symbol of nitrogen? ")).lower() # vika testin kysymys
    if N == 'n':
        print(Fore.GREEN + f"Your answer: '{N}' is correct!\n")
        print(Fore.GREEN + "Well done! Now they believe you and you can continue your journey.\n"
                           "Although that was close call!") # jos vastaa kaikkiin oikein
    else:
        currency_subtract(10, screen_name)
        distance_substract(1, screen_name)
        print(Fore.RED + "Your credibility vanished like ashes in the wind.\n"
                         "I hope you have some distance left, because aliens are again 1 distance step closer!")
    return check_if_game_over(screen_name)

#Alienratsia
def run_or_hide(screen_name):
    print(Fore.BLUE + f'''
    Your previous flight landed late due to weather conditions and there's only 15 minutes 
    before your next flight leaves. You are rushing to the next departure gate when you suddenly 
    see alien raid in front of you! There is very little you can do about in this situation, 
    you can either try to run past the raid like a madman or you can hide in the nearby trash can.
    ''')
    while True:
        decision = input(Fore.RESET + "So are you going to run or hide? (run/hide) ") #Pelaaja valitsee haluaako juosta koneeseen vai piiloutua ja odottaa seuraavaa.
        if decision == "run":
            print(Fore.RED + "Oh no! The aliens spotted you and now know exactly where you are.\n"
                             "Good thing is that the aliens didn't catch you. You lose 2 distance steps.\n")
            distance_substract(2, screen_name)
            break
        elif decision == "hide":
            print(Fore.GREEN + "Hurry up, jump in the trash can now! Try to make yourself comfortable\n"
                               "and wait for the raid to end.\nAfter that you can catch the next flight.\n"
                               "You lose 1 distance step. ")
            distance_substract(1, screen_name)
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "I believe that was not one of the options I gave you...")
    return check_if_game_over(screen_name)


def flight_cancelled(screen_name):
    print(Fore.BLUE + f'''
    You notice at the airport that your next flight has been cancelled! 
    the ticket seller at the airport tells you that you have two options to choose from! 
    Either you wait for a replacement flight which leaves tomorrow, 
    or you can purchase new ticket for another airline's flight which leaves in two hours.
    ''')

    while True:
        decision = input(Fore.RESET + "How about it? Do you wait or purchase a new ticket? (wait/new) ")
        if decision == "wait": #Menettää välimatkaa
            print(Fore.RED + "You spend the night sleeping uncomfortably on the airport floor.\n"
                             "You lose 1 distance step.")
            distance_substract(1, screen_name)
            break
        elif decision == "new": #Menettää valuuttaa
            print(Fore.RED + "You got your new ticket. But because you decided to bought a new ticket\n"
                             "from another airline, the previous company refuses to refund the old ticket.\n"
                             "You lose 10$. ")
            currency_subtract(10, screen_name)
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "I believe that was not one of the options I gave you...")
    return check_if_game_over(screen_name)

#Pitää muuttaa f --> C
def fahrenheit_to_celsius(screen_name):
    cursor = connect.cursor()
    game_sql = f"SELECT location, currency, alien_distance, in_possession FROM game WHERE screen_name='{screen_name}';"
    cursor.execute(game_sql)
    result = cursor.fetchall()

    norway = Fore.BLUE + f'''
    You finally got to Norway and found the ancient ingredient! But the journey is not over yet.
    Next, you have to transport it back to the laboratory in cuba. 
    Remember that the Scientists in Cuba reminded you, when you left that the ancient ingredient 
    must be stored in a cold pack all the time. They told you that under no circumstances should 
    the temperature of the container rise above +4 Celsius, else the ingredient will be ruined.
    So be careful with the ingredient!...In fact, if I were you, I would check the ingredient right away!
    '''
    for letter in norway:  # kirjain kerrallaan
        print(letter, end='', flush=True) # end: estää uuden rivin tulostamisen jokaisen kirjaimen jälkeen, flush: pakottaa tulostuksen heti eli näkyy välittömästi ilman puskurointia
        time.sleep(0.03) # aiheuttaa lyhyen viiveen jokaisen kirjaimen tulostuksen jälkeen
    print()

    print(Fore.RESET + "You notice that the cold pack is broken. it must have broken when you took it with you\n"
                       "Miraculously you found a new cold pack, but now you have to make sure that the ingredient\n"
                       "didn't warm up too much and become unusable.\n")
    print("Ingredient container's thermometer shows the temperature in Fahrenheit, but you don't understand them,\n"
          "so you have to convert them to Celsius to understand the current temperature.\n")
    print("According to the thermometer, the temperature is now 39 fahrenheits") #Pelaajalle kerrotaan valmiiksi F, jolloin hänen täytyy itse laskea mitä se on Celsiuksina

    while True:
        celsius = int(input(Fore.RESET + "What is the temperature in Celsius?\nHOX! Integers only!\n39 Fahrenheits: "))
        if celsius == 3: #Oikea vastaus
            print(Fore.GREEN + "What a relief! The ingredient looks fine and didn't warm up too much.")
            break
        else:
            print(Fore.RED + "Nope...Try again. oh by the way, for every wrong answer you lose 1 distance step.") #Pelaaja joutuu vastaamaan uudestaan
            distance_substract(1, screen_name)
            user_currency_distance(screen_name)
            if check_if_game_over_fahrenheit(screen_name) == False:
                break

    return check_if_game_over(screen_name)


def country_capital(screen_name):
    print(Fore.BLUE + '''
    Suddenly a child runs in front of you crying and asks for help. She tells you that 
    she has lost her family and can't find them anywhere. You don't have the heart to 
    refuse and you decide to help her. You notice an announcement device near by and it 
    would make it easier to find the child's family. But to use the device you must answer 
    following question correctly. 
    ''')
    def guess_capital(): # valitsee satunnaisen maan ja palauttaa kyseisen maan nimen ja pääkaupungin.
        country_list = [
            "Russia", "Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina",
            "Denmark", "Algeria", "Finland", "Greenland", "Sweden", "Vietnam", "Switzerland", "Nepal",
            "Italy", "Indonesia", "Belgium", "Bolivia", "Iran", "Mongolia", "Peru", "Spain", "Kazakhstan",
            "Germany", "United Kingdom", "Colombia", "Ethiopia", "Thailand", "Poland",
            "Japan", "Norway", "Egypt", "Greece", "Pakistan", "Chile", "South Korea", "Turkey", "New Zealand",
            "Zambia", "Canada", "Afghanistan", "Iceland", "France", "Somalia", "North Korea", "Ukraine",
            "Botswana", "Madagascar", "Cuba"
        ]
        country_name = random.choice(country_list)
        capital = CountryInfo(country_name).capital()
        return country_name, capital

    def check_answer(country, answer): # tarkistetaan vastaus
        if answer.lower() == country[1].lower(): #verrataan annettua ja oikeaa vastausta
            print(Fore.GREEN + "Yes, that's right! Child's family is rather quickly found through the announcement.\n"
                               "They are grateful to you and recognize you as a resistance member.\n"
                               "The family wants to help you and they warn you that aliens are lurking\n"
                               "at your next destination. Thanks to the tip, you can now take another route\n"
                               "and avoid the encounter with the aliens. You get 1 distance step.")
            distance_add(1, screen_name)
        else:
            print(Fore.RED + "Wrong, your geography seems to be rusty! And because of that \n"
                             "you can't make the announcement and it takes very long time to find the child's family.\n"
                             "Because it took so long, you missed your next flight. Aliens are 1 distance step closer.")
            distance_substract(1, screen_name)
        check_if_game_over(screen_name)

    country = guess_capital()
    answer = input(Fore.RESET + f"What is the capital of {country[0]}? ")
    check_answer(country, answer)
    return check_if_game_over(screen_name)


def suspicious_employee(screen_name):
    print(Fore.BLUE + f'''
    While walking to the next departure gate, one of the airport employee thinks you're a cleaner and asks
    you to take out pile of trash. You now have to decide whether to play along or tell her that you're not a cleaner.
    Remember that helping may benefit you, while refusing may cause problems. Or it could be the other way around, 
    who knows... Choose wisely.
    ''')

    while True:
        answer = input(Fore.RESET + "So are you going to take the trash out? (Y/N): ").lower()

        if answer == "y":
            print(Fore.GREEN + "You take out the trash and the employee thanks you for your help and gives you a tip.\n"
                               "You lose 1 distance step but gain 10$.")
            currency_add(10, screen_name)
            distance_substract(1, screen_name)
            break
        elif answer == "n":
            print(Fore.RED + "Employee apologizes for her mistake but becomes suspicious of you and\n"
                             "wants to talk to you for a very long time, before letting you continue your journey.\n"
                             "You lose 2 distance steps")
            distance_substract(2, screen_name)
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid choice.")
    return check_if_game_over(screen_name)


def makeover_time(screen_name):
    print(Fore.BLUE + f'''
    In this airport you come across makeover experts and they offer you opportunity to change 
    your appearance for a some amount of currency. Makeover might help you fool aliens, 
    giving you more distance to them. So let's take a look see what experts have to offer. 
    ''')

    print(Fore.RESET + "Welcome to the makeover studio!")

    while True:
        print("\nMake your choice regarding the makeover:")
        print("1. Change one thing (costs 10$, may or may not help)")
        print("2. Change two things (costs 20$, helps at least somewhat)")
        print("3. Complete makeover (costs 50$, definitely helps!)")
        print("4. I'll settle for how I look now\n")

        choice = input("Which options sounds best? (1-4): ")

        sql = f"SELECT currency FROM game WHERE screen_name = '{screen_name}'"
        cursor = connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if choice == "1":
            if result[0][0] >= 10:
                currency_subtract(20, screen_name)
                print(Fore.GREEN + "One thing changed! I'm not sure if that will help you...")
                input("press enter to check: ")
                check = random.randint(1, 2) #arvotaan auttaako muutos pelaajaa
                if check == 1:
                    print("Change seems to have worked this time. you get 1 distance step")
                    distance_add(1, screen_name)
                else:
                    print("As suspected, the change didn't help you")
                return check_if_game_over(screen_name) # Lopetetaan suoritus, kun yksi muutos on tehty.
            else:
                print(Fore.RED + "You are too poor to change one thing.")
        elif choice == "2":
            if result[0][0] >= 20:
                currency_subtract(20, screen_name)
                distance_add(2, screen_name)
                print(Fore.GREEN + "Two things changed, that works pretty well! you get 2 distance steps")
                return check_if_game_over(screen_name) # Lopetetaan suoritus, kun kaksi muutosta on tehty.
            else:
                print(Fore.RED + "You are too poor to change two things.")
        elif choice == "3":
            if result[0][0] >= 50:
                currency_subtract(50, screen_name)
                distance_add(3, screen_name)
                print(Fore.GREEN + "Complete makeover done and Wow! You look like a completely different person!\n "
                                   "you get 3 distance steps.")
                return check_if_game_over(screen_name) # Lopetetaan suoritus, kun täydellinen muodonmuutos on tehty.
            else:
                print(Fore.RED + "You are too poor for a complete makeover.")
        elif choice == "4":
            print(Fore.LIGHTYELLOW_EX + "Thanks for your visit!")
            return check_if_game_over(screen_name) # Lopetetaan suoritus, jos käyttäjä ei halua muuttaa mitään.
        else:
            print(Fore.LIGHTYELLOW_EX + "That's not an option. Try again and pick number 1-4.")

def hiding_closet(screen_name):
    print(Fore.BLUE + f'''
    You encounter a fugitive at the airport, who is fleeing from security guard. 
    He wants to hide in the janitor's closet, which is locked with a three-digit code. 
    You have three attempts to answer correctly, or the door will be permanently locked. 
    If you manage to open the door, the fugitive might reward you for your help. 
    Oh and here's a little tip for you, the number can't be bigger than 5. Now get to work!
    ''')
    code = [1, 2, 4]
    player_code = []
    attempts = 1
    number1 = int(input(Fore.RESET + "Enter the first number: "))
    player_code.append(number1)
    number2 = int(input(Fore.RESET + "Enter the second number: "))
    player_code.append(number2)
    number3 = int(input(Fore.RESET + "Enter the third number: "))
    player_code.append(number3)

    while player_code != code and attempts < 3:
        print(Fore.RED + "Invalid code! Try again!")
        if number1 == code[0]:
            print(Fore.GREEN + "First number is correct!")
        if number2 == code[1]:
            print(Fore.GREEN + "Second number is correct!")
        if number3 == code[2]:
            print(Fore.GREEN + "Third number is correct!")
        player_code.clear()
        number1 = int(input(Fore.RESET + "Enter the first number: "))
        player_code.append(number1)
        number2 = int(input("Enter the second number: "))
        player_code.append(number2)
        number3 = int(input("Enter the third number: "))
        player_code.append(number3)
        attempts += 1
    if attempts == 3 and player_code != code:
        print(Fore.RED + "OH NO! look what you did, the door is now permanently locked and the fugitive got caught!\n "
                         "No rewards for you!")
        return check_if_game_over(screen_name)
    else:
        print(Fore.GREEN + "WOW! You did it! You managed to open the door and fugitive can now hide. He gives you 20$")
        currency_add(20, screen_name)
        return check_if_game_over(screen_name)


def crazy_dice(screen_name):
    print(Fore.BLUE + f'''
    You encounter a quirky street artist at the airport, and he wants to challenge you to a dice roll for money. 
    The one who gets the higher total of two dice wins and takes the loser's money. The bet is 10$.''')

    input(f'''
    The quirky street artist won't let you go before you accept the challenge and the 
    aliens are catching up. Hurry and accept the challenge by pressing enter!\n ''')

    while True:
        print(Fore.RESET + "The quirky street artist begins...")
        street_artist_dice1 = random.randint(1, 6)
        street_artist_dice2 = random.randint(1, 6)
        street_artist_total = street_artist_dice1 + street_artist_dice2
        print(f"The quirky street artist got {street_artist_dice1} and {street_artist_dice2}\n"
              f"making the total of {street_artist_total}")
        input("Now it's your turn. Press enter to roll! ")
        player_dice1 = random.randint(1, 6)
        player_dice2 = random.randint(1, 6)
        player_dice_total = player_dice1 + player_dice2
        if street_artist_total < player_dice_total:
            print(Fore.GREEN + f"Congrats! you rolled a {player_dice1} and {player_dice2}\n"
                               f"making the total of {player_dice_total}! You won 10$!")
            currency_add(10, screen_name)
            return check_if_game_over(screen_name)
        if street_artist_total > player_dice_total:
            print(Fore.RED + f"Oh no! You rolled {player_dice1} and {player_dice2}\n"
                             f"making the total {player_dice_total}. You lost your 10$ !")
            currency_subtract(10, screen_name)
            return check_if_game_over(screen_name)
        else:
            print(Fore.YELLOW + f"Oij! You rolled {player_dice1} and {player_dice2}\n"
                                f"making the total same {player_dice_total}. Let's try again!")

def resistance_test(screen_name):
    print(Fore.BLUE + f'''
    You bump into another resistance member. He is skeptical if you are truly part of the 
    resistance and wants to make sure before helping you further. By answering his question
    correctly, he promise to help you distract the aliens. Hurry up! The question is:
    ''')

    correct_answer = "dr alex zen"
    answer = input(Fore.RESET + "What is the name of the lead scientist of the resistance? ").lower()
    if answer == correct_answer:
        print(Fore.GREEN + "That is correct! You have proved that you're true resistance member and\n"
                           "your new friend will help you forward. you gain 1 distance step")
        distance_add(1, screen_name)
    elif answer == "alex zen":
        print(Fore.GREEN + "That is correct! You have proved that you're true resistance member and\n"
                           "your new friend will help you forward. gain 1 distance step")
        distance_add(1, screen_name)
    else:
        print(Fore.RED + "That's not it! I guess you didn't read the lore properly...\n"
                         "Well, no help for you this time. Carry on.")
    return check_if_game_over(screen_name)

