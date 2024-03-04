# tehtävät lol
import mysql.connector
from connection import connect
import game_functions

def challenge_currency_help(screen_name): # tehtävä valuutan vaihto #fuck you
    print("You ran into a world travler in distress. They need your help with currency.")
    answer = input("How much is 10 euros in yens?")
    mycursor = connect.cursor() # osotetaa tietokantaa
    if answer == 1630: # jos käyttäjän vastaus vastaa oikeaa vastausta
        print("That's right! The traveler grants you with a reward.")
        challenge_currency_add(10, screen_name) # lisätään valuuttaan 10 €
    else:
        print("Oh no! That's not quite right...")
        print("The traveler fooled you. It was a pickpocket bluffing you. You lost 20 $")
        challenge_currency_subtract(20, screen_name) # vähennetään valuuttaa -20


def challenge_recognized(player_name): # tehtävä sut tunnistetaan
    print("At the check-in one of the employees recognizes you.\nThey give you a dirty look as you lay your eyes on the pin on their vest\n'END TO PLANET EARTH' it says\nDo they recognize you from tv?")
    answer = int(input("You can either 1. bribe them or 2. play it cool. Choose (1/2)\n"))
    mycursor = connect.cursor() # osotetaa tietokantaa
    if answer == 1: # jos lahjoo
        challenge_currency_subtract(10, screen_name) #vähennetään -10
        print("Offering a bribe helps you stay low but now your pockets are 10$ lighter")
    elif answer == 2:
        challenge_distance_substract(1, screen_name)
        print("You didn't want to make a scene and tried to play it cool.\nThe employee lets their anti-earth friends know about your location.\nThe aliens are closer to you.")
    else:
        print("That wasn't an option silly...")
    return

def challenge_chemist(player_name): # tehtävä huijaa olevasi kemisti
    print("The airport security question you. You don't trust them so you lie.\nYou tell them you're a chemist and they test you.")
    mycursor = connect.cursor() # osotetaa tietokantaa
    Fe = str(input("What is the chemical symbol of iron?\n")).lower() # eka testin kysymys
    if Fe == 'fe':
        print(Fe)
        Au = str(input("What is the chemical symbol of gold?\n")).lower() # toka testin kysymys
        if Au == 'au':
            print(Au)
            N = str(input("What is the chemical symbol of nitrogen?\n")).lower() # vika testin kysymys
            if N == 'n':
                print(N)
                print("Well done! They believe you and you leave empty handed. Good thing you barely make it to your next flight!") # jos vastaa kaikkiin oikein
            else: # kolmannen epäonnistuminen
                challenge_currency_subtract(10, screen_name)
                challenge_distance_substract(1, screen_name)
                print("They don't believe you. You lost $ and the aliens are closer to you")
        else: # tokan epäonnistuminen
            challenge_currency_subtract(10, screen_name)
            challenge_distance_substract(1, screen_name)
            print("They don't believe you. You lost $ and the aliens are closer to you")
    else: # ekan epäonnistuminen
        challenge_currency_subtract(10, screen_name)
        challenge_distance_substract(1, screen_name)
        print("They don't believe you. You lost $ and the aliens are closer to you")
    return

#Alienratsia
def challenge_distance_alienraid():
    print("There's only few minutes before your next flight. On your way to the departure gate you face an alien raid!")
    print(" You can run to your flight or hide in the trash can and wait for the next flight. ")

    decision = input("Do you run or hide? ") #Pelaaja valkkaa haluaako juosta koneeseen vai piiloutua ja odottaa seuraavaa.
    if decision == "run":
        print("Oh no! Aliens notice you and now they know where you are going. -2 distance ")
        challenge_distance_substract(2, screen_name)
    elif decision == "hide":
        print("Now run to hide. You need to wait for the next flight. -1 distance")
        challenge_distance_substract(1, screen_name)

#challenge_distance_alienraid()

#Pelaajan seuraava kone perutaan, pitää valita menettääkö valuuttaa vai välimatkaa
def challenge_distance_cancelledflight():
    print("The next flight has been cancelled! ")
    print("You can wait for the next one or purchase a new ticket.")
    decision = input("Do you wait or purchase a new ticket? ")
    if decision == "wait": #Menettää välimatkaa
        print("Better luck next time. Let's hope the next one is on time. -1 distance ")
        challenge_distance_substract(1, screen_name)
    elif decision == "purchase": #Menettää valuuttaa
        print("You get on another plane. New tickets cost you 10€. ")
        challenge_currency_subtract(10, screen_name)


#challenge_distance_cancelledflight()

#Pitää muuttaa f --> C
def fahrenheit_to_celsius():
    print("Ancient ingredient must be stored in a cold pack, but you broke it! You found a new one, but now you need to make sure the ingredient didn't warm up.")
    print("Thermometer shows the temperature in fahrenheits, but you need to convert them into celsius so you can read them.")
    print("Temperature in fahrenheits is 39") #Pelaajalle kerrotaan valmiiksi F, jolloin hänen täytyy itse laskea mitä se on Celsiuksina
    while True:
        celsius = float(input("What is the temperature in Celsius?: "))
        if celsius == 3.0: #Oikea vastaus
            print("Amazing! The ingredient looks fine.")
            break
        else:
            print("Try again.") #Pelaaja joutuu vastaamaan uudestaan

#fahrenheit_to_celsius()

import random
from countryinfo import CountryInfo

def country_capital():
    # Tulostetaan tilanne lentokentällä
    print(
        "At the airport, a child comes to you and asks for help. She tells you that she has lost her family and can't find them. Solve the following question to help the child.")

#Valitaan satunnaisen maa listalta ja hakee sen pääkaupungin countryinfo-moduulin avulla.
    country_list = [
        "Russia", "Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina",
        "Denmark", "Algeria", "Finland", "Greenland", "Sweden", "Vietnam", "Switzerland", "Nepal",
        "Italy", "Indonesia", "Belgium", "Bolivia", "Iran", "Mongolia", "Peru", "Spain", "Kazakhstan", "Germany",
        "United Kingdom", "South Africa", "Colombia", "Ethiopia", "Thailand", "Poland", "Japan", "Norway",
        "Egypt", "Greece", "Pakistan", "Chile", "South Korea", "Turkey", "New Zealand", "Zambia",
        "Canada", "Afghanistan", "Iceland", "France", "Somalia", "North Korea",
        "Ukraine", "Botswana", "Madagascar"
    ]
    country_name = random.choice(country_list)
    capital = CountryInfo(country_name).capital()
    return country_name, capital


def check_answer(country, answer):
    # Tarkistetaan vastaus ja annetaan vastauksen mukainen teksti
    if answer.lower() == country[1].lower():
        print("Correct! The child's family tells you that aliens are lurking at your next destination. Thanks to the tip, you can now take another route and avoid the encounter with the aliens. You get +1 distance point.")
        challenge_distance_add(1, screen_name)
    else:
        print("Wrong! Unfortunately, you miss your next flight because it took more time to help the child. Aliens advance 1 distance point closer.")
        challenge_distance_substract(1, screen_name)


def guess_the_capital():
    #aloittaa itse pelin kysymällä pelaajalta satunnaisen maan pääkaupunkia ja tarkistaa vastauksen.
    country = country_capital()
    answer = input(f"What is the capital of {country[0]}? ")

    check_answer(country, answer)


#kutsutaan pelin aloittavaa funktiota, jotta peli voidaan pelata
guess_the_capital()

def suspicious_employee():
    print("airport clerk thinks you're an airport employee and they ask you to take out pile of trash")

    answer = input("Do you want to help? (Y/N): ").lower()

    if answer == "y":
        print("You take out the trash and the clerk thanks you for your help. You lose one distance point but gain x amount of currency.")
        challenge_currency_add(10, screen_name)
        challenge_distance_substract(1, screen_name)
    elif answer == "n":
        print("the clerk becomes suspicious of you and wants to talk to you for a very long time before letting you continue your journey. you lose 2 distance points")
        challenge_distance_substract(2, screen_name)
    else:
        print("invalid choice. select y or n.")


#Ohjelma käynnistyy tästä
suspicious_employee()


print("In the airport you come across makeover experts and they offer you opportunity to change your appearance for a small amount of currency. Let's see what they have to offer. ")
def makeover_time(currency, x, y):
    print("Welcome to the makeover studio!")
    print("Your currency:", currency)

    while True:
        print("\nMake your choice regarding the makeover:")
        print("1. Change one thing (costs x currency)")
        print("2. Change two things (costs 2 * x currency)")
        print("3. Complete makeover (costs y currency)")
        print("4. Don't want to change anything")

        choice = input("Your choice (1-4): ")

        if choice == "1":
            if currency >= x:
                challenge_currency_subtract(20, screen_name)
                challenge_distance_add(1, screen_name)
                print("One thing changed!")
                return  #Lopetetaan suoritus, kun yksi muutos on tehty.
            else:
                print("You don't have enough money to change one thing.")
        elif choice == "2":
            if currency >= 2 * x:
                challenge_currency_subtract(20, screen_name)
                challenge_distance_add(2, screen_name)
                print("Two things changed!")
                return  #Lopetetaan suoritus, kun kaksi muutosta on tehty.
            else:
                print("You don't have enough money to change two things.")
        elif choice == "3":
            if currency >= y:
                challenge_currency_subtract(50, screen_name)
                challenge_distance_add(3, screen_name)
                print("Complete makeover done!")
                return  #Lopetetaan suoritus, kun täydellinen muodonmuutos on tehty.
            else:
                print("You don't have enough money for a complete makeover.")
        elif choice == "4":
            print("Thanks for your visit!")
            return  #Lopetetaan suoritus, jos käyttäjä ei halua muuttaa mitään.
        else:
            print("Invalid choice. Try again and pick number 1-4.")

# kutsutaan funktio ja testataan se
currency = 100  #Pelaajan valuutta
x = 10  #Yhden asian muutoksen hinta
y = 50  #Täydellisen muodonmuutoksen hinta
makeover_time(currency, x, y)



def challenge_hiding_closet():
    print('''You encounter a fugitive at the airport fleeing from aliens. 
He wants to hide in the airport janitor's closet, which is locked with a three-digit code. 
You have three attempts to answer correctly, or the door will lock permanently. 
If you manage to open the door, the fugitive might reward you for your help! 
Get to work! Hurry!
''')
    code = [1, 2, 4]
    player_code = []
    attemps = 1
    number1 = int(input("Enter the first number: "))
    player_code.append(number1)
    number2 = int(input("Enter the second number: "))
    player_code.append(number2)
    number3 = int(input("Enter the third number: "))
    player_code.append(number3)

    while player_code != code and attemps < 3:
        print("Invalid code! Try again!")
        if number1 == code[0]:
            print("First number is correct!")
        if number2 == code[1]:
            print("Second number is correct!")
        if number3 == code[2]:
            print("Third number is correct!")
        player_code.clear()
        number1 = int(input("Enter the first number: "))
        player_code.append(number1)
        number2 = int(input("Enter the second number: "))
        player_code.append(number2)
        number3 = int(input("Enter the third number: "))
        player_code.append(number3)
        attemps += 1
    if attemps == 3 and player_code != code:
        print("You idiot! You locked the fucking door!")
    else:
        print("WOW! You did it! You managed to open the door and earned 20€!")
        challenge_currency_add(20, screen_name)


def challenge_crazydice():
    print('''You encounter a quirky street artist at the airport, and he wants to challenge you 
to a dice roll for money. The one who gets the higher total of the two dice wins and takes the loser's money. 
The bet is 10 euros.''')

    start = input("The quirky street artist won't let you go before you accept the challenge and the "
                  "aliens are catching up. Hurry and accept the challenge by pressing enter! ")
    if start == "":
        print("The quirky street artist begins...")
        street_artist_dice1 = random.randint(1,6)
        street_artist_dice2 = random.randint(1, 6)
        street_artist_total = street_artist_dice1 + street_artist_dice2
        print(f"The quirky street artist got {street_artist_dice1} and {street_artist_dice2} "
              f"making the total of {street_artist_total}")

        player_roll = input("Now it's your turn. Press enter to roll!")
        if player_roll == "":
            player_dice1 = random.randint(1, 6)
            player_dice2 = random.randint(1,6)
            player_dice_total = player_dice1 + player_dice2
            if street_artist_total < player_dice_total:
                print(f"Congrats! you rolled a {player_dice1} and {player_dice2} making the total of {player_dice_total}! "
                      f"You won 10€!")
                challenge_currency_add(10, screen_name)
            else:
                print(f"Oh no! You rolled {player_dice1} and {player_dice2} making the total {player_dice_total}. "
                      f"You lost your 10€!")
                challenge_currency_subtract(10, screen_name)


def challenge_resistance_test():
    print('''
    You encounter another resistance member. He is skeptical if you are truly part of the resistance 
    and wants to make sure before helping you further. By answering his question correctly, you gain 
    more distance from the aliens. Hurry up! The question is:
    ''')
    correct_answer = "Dr Alex Zen"
    answer = input("What is the name of the lead scientist of the resistance? ")
    if answer == correct_answer:
        print("That is correct! You have proved that you're true resistance member and gained +1 distance")
        challenge_distance_add(1, screen_name)
    elif answer == "Alex Zen":
        print("That is correct! You have proved that you're true resistance member and gained +1 distance")
        challenge_distance_add(1, screen_name)
    else:
        print("That's not it! Did you even read the lore in the beginning...No help for you this time. Curry on.")











