# tehtävät lol

def challenge_currency_help(): # tehtävä valuutan vaihto
    print("You ran into a world travler in distress. They need your help with currency.")
    answer = input("How much is 10 euros in yens?")
    yen = 1630
    currency = 100
    if answer == yen: # jos käyttäjän vastaus vastaa oikeaa vastausta
        print("That's right! The traveler grants you with a reward.")
        currency = currency + 20 # lisää rahaa
    else:
        print("Oh no! That's not quite right...")
        print("The traveler fooled you. It was a pickpocket bluffing you. You lost 20 $")
        currency = currency - 20 # vähennetään rahaa
    return

def challenge_recognized(): # tehtävä sut tunnistetaan
    currency = 100
    distance = 100
    print("At the check-in one of the employees recognizes you.\nThey give you a dirty look as you lay your eyes on the pin on their vest\n'END TO PLANET EARTH' it says\nDo they recognize you from tv?")
    answer = int(input("You can either 1. bribe them or 2. play it cool. Choose (1/2)\n"))
    if answer == 1: # jos lahjoo
        currency = currency - 10
        print("Offering a bribe helps you stay low but now your pockets are 10$ lighter")
    elif answer == 2:
        distance = distance - 10
        print("You didn't want to make a scene and tried to play it cool.\nThe employee lets their anti-earth friends know about your location.\nThe aliens are closer to you.")
    else:
        print("That wasn't an option silly...")
    return

def challenge_chemist(): # tehtävä huijaa olevasi kemisti
    currency = 100
    distance = 100
    print("The airport security question you. You don't trust them so you lie.\nYou tell them you're a chemist and they test you.")
    Fe = str(input("What is the chemical symbol of iron?\n")).lower() # eka testin kysymys
    if Fe == 'fe':
        print(Fe)
        Au = str(input("What is the chemical symbol of gold?\n")).lower() # toka testin kysymys
        if Au == 'au':
            print(Au)
            N = str(input("What is the chemical symbol of nitrogen?\n")).lower() # vika testin kysymys
            if N == 'n':
                print(N)
                print("They believe you and you leave empty handed. Good thing you barely make it to your next flight!") # jos vastaa kaikkiin oikein
            else: # kolmannen epäonnistuminen
                distance = distance - 10
                currency = currency - 10
                print("They don't believe you. You lost $ and the aliens are closer to you")
        else: # tokan epäonnistuminen
            distance = distance - 10
            currency = currency - 10
            print("They don't believe you. You lost $ and the aliens are closer to you")
    else: # ekan epäonnistuminen
        distance = distance - 10
        currency = currency - 10
        print("They don't believe you. You lost $ and the aliens are closer to you")
    return

#Alienratsia
def challenge_distance_alienraid():
    print("There's only few minutes before your next flight. On your way to the departure gate you face an alien raid!")
    print(" You can run to your flight or hide in the trash can and wait for the next flight. ")

    decision = input("Do you run or hide? ")
    if decision == "run":
        print("Oh no! Aliens notice you and now they know where you are going. -2 distance ")
    elif decision == "hide":
        print("Now run to hide. You need to wait for the next flight. -1 distance")

challenge_distance_alienraid()
#Pelaajan seuraava kone perutaan, pitää valita menettääkö valuuttaa vai välimatkaa
def challenge_distance_cancelledflight():
    print("The next flight has been cancelled! ")
    print("You can wait for the next one or purchase a new ticket.")
    decision = input("Do you wait or purchase a new ticket? ")
    if decision == "wait":
        print("Better luck next time. Let's hope the next one is on time. -1 distance ")
    elif decision == "purchase":
        print("You get on another plane. New tickets cost you 50€. ")

challenge_distance_cancelledflight()

#Pitää muuttaa f --> C
def fahrenheit_to_celsius():
    print("Ancient ingredient must be stored in a cold pack, but you broke it! You found a new one, but now you need to make sure the ingredient didn't warm up.")
    print("Thermometer shows the temperature in fahrenheits, but you need to convert them into celsius so you can read them.")
    print("Temperature in fahrenheits is 39")
    while True:
        celsius = float(input("What is the temperature in Celsius?: "))
        if celsius == 3.0:
            print("Amazing! The ingredient looks fine.")
            break
        else:
            print("Try again.")

fahrenheit_to_celsius()
