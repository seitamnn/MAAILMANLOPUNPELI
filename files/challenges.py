# Tehtävät lolleroiset
import mysql.connector
from connection import connect
from game_functions import distance_add, distance_substract, currency_add, currency_subtract
import random
from countryinfo import CountryInfo

def currency_converter(screen_name): # tehtävä valuutan vaihto #fuck you
    print('''
    You are in your own thoughts when accidentally bump into strange looking world traveler at the airport. 
    He asks for your help with the currency conversion and you decide to help him. 
    Let's see what kind of problem he has.
    ''')

    answer = input("How much is 10 euros in yens?")
    mycursor = connect.cursor() # osotetaa tietokantaa
    if answer == 1630: # jos käyttäjän vastaus vastaa oikeaa vastausta
        print("That's right! The traveler will be very grateful and give you currency for the effort. You got 10 $, hooray!")
        currency_add(10, screen_name) # lisätään valuuttaan 10 €
    else:
        print(" Oh no, you're not quite right...")
        print("The traveler fooled you. He was a pickpocket who took some currency from you. You lost 20 $")
        currency_subtract(20, screen_name) # vähennetään valuuttaa -20


def recognized(screen_name): # tehtävä sinut tunnistetaan
    print('''
    At the airport check-in one of the employees recognizes you. He looks at you disapprovingly. 
    You notice a pin on his chest. where it says 'END TO PLANET EARTH' He probably recognizes you from the news...
    because of the mission you've been on it a lot lately. What should you do about it?
    ''')

    answer = int(input("You can either 1. try to bribe him or 2. Ignore the situation as if nothing had happened. Now Choose (1/2)\n"))
    mycursor = connect.cursor() # osotetaa tietokantaa
    if answer == 1: # jos lahjoo
        currency_subtract(10, screen_name) #vähennetään -10
        print("The bribes was useful and helps you keep a low profile. At the price that your wallet is now 10$ lighter")
    elif answer == 2:
        distance_substract(1, screen_name)
        print("You tried to ignore the situation completely.\nThe employee lets their anti-earth friends know about your location.\nNow aliens are one step closer to you.")
    else:
        print("I believe that was not one of the options i gave you...")
    return


def fake_chemist(screen_name): # tehtävä huijaa olevasi kemisti
    print('''
    At the airport security check, the metal part of the ingredient container causes problems.
    Container arouses the interest of employees and they start asking you questions about it.
    You panic, and decide to lie and explain that you're a chemist and that's why you have the container with you.
    The employees don't fully believe you and they decide to test you. 
    ''')

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
                print("Well done! Now they believe you and you can continue your journey. Luckily you made it to your next flight, even though it was close call!") # jos vastaa kaikkiin oikein
            else: # kolmannen epäonnistuminen
                currency_subtract(10, screen_name)
                distance_substract(1, screen_name)
                print("Your credibility vanished like ashes in the wind. Oh no, the aliens found and captured you! ")
        else: # tokan epäonnistuminen
            currency_subtract(10, screen_name)
            distance_substract(1, screen_name)
            print("Your credibility has almost entirely vanished. There's no room for errors now! and i don't want to worry you, but the aliens have taken another step forward you and are just around the corner!")
    else: # ekan epäonnistuminen
        currency_subtract(10, screen_name)
        distance_substract(1, screen_name)
        print("Your credibility begins to diminish. Carefully now!. By the way, just so you know the aliens are one step closer now!")
    return

#Alienratsia
def run_or_hide(screen_name):
    print('''
    Your previous flight landed late due to weather conditions and there's only 15 minutes before your 
    next flight leaves. You are rushing to the next departure gate when you suddenly see alien raid in front of you!
    There is very little you can do about in this situation, you can either try to run like a madman or 
    hide in the nearby trash can. 
    ''')

    decision = input("So are you going to run or hide? ") #Pelaaja valkkaa haluaako juosta koneeseen vai piiloutua ja odottaa seuraavaa.
    if decision == "run":
        print("Oh no! The aliens spotted you and now know exactly where you are. Good thing is that the aliens didn't catch you and that you made it to your flight. Unfortunately you will lose 2 distance point ")
        distance_substract(2, screen_name)
    elif decision == "hide":
        print("Hurry up, jump in the trash can now! Try to make yourself comfortable and wait for the raid to end. After that you can catch the next flight. you lose 1 distance point")
        distance_substract(1, screen_name)

#challenge_distance_alienraid()

#Pelaajan seuraava kone perutaan, pitää valita menettääkö valuuttaa vai välimatkaa
def flight_cancelled(screen_name):
    print('''
    You notice at the airport that your next flight has been cancelled! 
    the ticket seller at the airport tells you that you have two options to choose from! 
    Either you wait for a replacement flight which leaves tomorrow, or you can purchase more expensive ticket 
    for another airline which leaves in two hours.
    ''')

    decision = input("How about it? Do you wait or purchase a new ticket? ")
    if decision == "wait": #Menettää välimatkaa
        print("it's a shame that this happened, hopefully this won't happen again. you lose 1 distance ")
        distance_substract(1, screen_name)
    elif decision == "purchase": #Menettää valuuttaa
        print("You bought a new ticket and got on the plane. Because you decided to choose a new ticket from another airline, the previous company refuses to refund the old ticket. New tickets cost you 10€. ")
        currency_subtract(10, screen_name)


#flight_cancelled()

#Pitää muuttaa f --> C
def fahrenheit_to_celsius(screen_name):
    print('''
    You've finally found the ancient ingredient! But danger is not over yet, and it's not time to celebrate. 
    Next, you still need to transport it back to the laboratory to save humanity from certain doom. 
    Remember that the Scientists in Cuba reminded you when you left that the ancient ingredient must be stored in 
    a cold pack all the time. They told you that under no circumstances should the temperature of the container rise 
    above +4 Celsius, otherwise the ingredient will be ruined.
    So now it's time to go back to cuba!
    Remember to be careful with the ingredient!...In fact, if I were you, I would check the ingredient right away!
    ''')

    print("Now you notice that you have broke the cold pack, when you took it with you! Miraculously you found a new cold pack, but now you have to make sure that the ingredient didn't warm up too much and become unusable.")
    print("Ingredient container's thermometer shows the temperature in fahrenheits and you don't understand them at all, so you have to convert them into celsius so that you understand something about the meter.")
    print("According to the thermometer, the temperature is now 39 fahrenheits") #Pelaajalle kerrotaan valmiiksi F, jolloin hänen täytyy itse laskea mitä se on Celsiuksina
    while True:
        celsius = float(input("What is the temperature in Celsius?: "))
        if celsius == 3.0: #Oikea vastaus
            print("Amazing! The ingredient looks fine and didn't warm up too much.")
            break
        else:
            print("That's not it...Try again.") #Pelaaja joutuu vastaamaan uudestaan

def country_capital(screen_name):
    print('''
    Suddenly a child runs in front of you crying and asks for help. She tells you that she has lost her family 
    and can't find them anywhere. You don't have the heart to refuse and you decide to help her.
    Following question will help you navigate in the airport. 
    ''')

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


def check_answer(country, answer, screen_name):
    # Tarkistetaan vastaus ja annetaan vastauksen mukainen teksti
    if answer.lower() == country[1].lower():
        print("Wow, you did it! child's family is rather quickly found. They are grateful to you and recognize you as a resistance soldier. The family wants to help you and they tell you that aliens are lurking at your next destination. Thanks to the tip, you can now take another route and avoid the encounter with the aliens. You get +1 distance point.")
        distance_add(1, screen_name)
    else:
        print("Wrong, your geography seems to be rusty! And because of that, you miss your next flight because it took too long to find the family. Aliens advance 1 distance point closer.")
        distance_substract(1, screen_name)


def guess_the_capital(screen_name):
    #aloittaa itse pelin kysymällä pelaajalta satunnaisen maan pääkaupunkia ja tarkistaa vastauksen.
    country = country_capital()
    answer = input(f"What is the capital of {country[0]}? ")
    check_answer(country, answer)


def suspicious_employee(screen_name):
    print('''
    while walking to the next departure gate, one airport employee thinks you're an airport cleaner and 
    they ask you to take out pile of trash. What you should do? Remember that helping may benefit you, 
    while refusing may cause problems. Or it could be the other way around, who knows... Choose wisely.
    ''')

    answer = input("What do you want to do? (Y/N): ").lower()

    if answer == "y":
        print("You take out the trash and the clerk thanks you for your help. You lose one distance point but gain x amount of currency.")
        currency_add(10, screen_name)
        distance_substract(1, screen_name)
    elif answer == "n":
        print("employee becomes suspicious of you and wants to talk to you for a very long time before letting you continue your journey. you lose 2 distance points")
        distance_substract(2, screen_name)
    else:
        print("invalid choice. select y or n.")


def makeover_time(currency, x, y, screen_name):
    print('''
    In the airport you come across makeover experts and they offer you opportunity to change your appearance 
    for a small amount of currency. Let's see what they have to offer. 
    ''')

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
                currency_subtract(20, screen_name)
                distance_add(1, screen_name)
                print("One thing changed, not sure if that helps...")
                return  #Lopetetaan suoritus, kun yksi muutos on tehty.
            else:
                print("You don't have enough money to change one thing.")
        elif choice == "2":
            if currency >= 2 * x:
                currency_subtract(20, screen_name)
                distance_add(2, screen_name)
                print("Two things changed, that works pretty well!")
                return  #Lopetetaan suoritus, kun kaksi muutosta on tehty.
            else:
                print("You don't have enough money to change two things.")
        elif choice == "3":
            if currency >= y:
                currency_subtract(50, screen_name)
                distance_add(3, screen_name)
                print("Complete makeover done and Wow! You look like a completely different person!")
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



def hiding_closet(screen_name):
    print('''
    You encounter a fugitive at the airport fleeing from aliens. 
    He wants to hide in the airport janitor's closet, which is locked with a three-digit code. 
    You have three attempts to answer correctly, or the door will lock permanently. 
    If you manage to open the door, the fugitive might reward you for your help! 
    Get to work! Hurry!
    ''')
    code = [1, 2, 4]
    player_code = []
    attempts = 1
    number1 = int(input("Enter the first number: "))
    player_code.append(number1)
    number2 = int(input("Enter the second number: "))
    player_code.append(number2)
    number3 = int(input("Enter the third number: "))
    player_code.append(number3)

    while player_code != code and attempts < 3:
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
        attempts += 1
    if attempts == 3 and player_code != code:
        print("NO! now look what you did! You locked the door!")
    else:
        print("WOW! You did it! You managed to open the door and earned 20€!")
        currency_add(20, screen_name)


def crazy_dice(screen_name):
    print('''
    You encounter a quirky street artist at the airport, and he wants to challenge you 
    to a dice roll for money. The one who gets the higher total of the two dice wins and takes the loser's money. 
    The bet is 10 euros.
    ''')

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
                currency_add(10, screen_name)
            else:
                print(f"Oh no! You rolled {player_dice1} and {player_dice2} making the total {player_dice_total}. "
                      f"You lost your 10€!")
                currency_subtract(10, screen_name)

def resistance_test(screen_name):
    print('''
    You bump into another resistance member. He is skeptical if you are truly part of the resistance 
    and wants to make sure before helping you further. By answering his question correctly, you gain 
    more distance from the aliens. Hurry up! The question is:
    ''')
    correct_answer = "Dr Alex Zen"
    answer = input("What is the name of the lead scientist of the resistance? ")
    if answer == correct_answer:
        print("That is correct! You have proved that you're true resistance member and your new friend will help you forward. you gain +1 distance")
        distance_add(1, screen_name)
    elif answer == "Alex Zen":
        print("That is correct! You have proved that you're true resistance member and your new friend will help you forward. gain +1 distance")
        distance_add(1, screen_name)
    else:
        print("That's not it! I guess you didn't read the lore in the beginning...Well, no help for you this time. Curry on.")

