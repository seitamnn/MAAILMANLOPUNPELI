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


from countryinfo import CountryInfo
import random

# Tulostetaan tilanne lentokentällä
print("at the airport, child comes to you and ask for help. She tells you that she has lost her family and can't find you. solve the following question to help the child ")

def country_capital():
    #Arvotaan satunnainen maa ja haetaan sen pääkaupunki
    country_name = random.choice(list(CountryInfo().all()))
    capital = CountryInfo(country_name).capital()
    return country_name, capital

def check_answer(country, answer):
    #Tarkistetaan vastaus ja annetaan vastauksen mukainen teksti
    if answer.lower() == country[1].lower():
        print("Correct! the kids family tells you that aliens are lurking at your next destination. thanks to the tip you can now take another route and avoid the encounter whit the aliens. you get +1 distance point")
    else:
        print("Wrong! Unfortunately, you miss your next flight, because it took more time to help the child . Aliens advance 1 dictance point closer.")

def guess_the_capital():
    #pelataan itse peliä
    country = country_capital()
    answer = input(f"What is the capital of {country[0]}? ")

    check_answer(country, answer)

#kutsutaan funktiota ja testataan se
guess_the_capital()



def suspicious_employee():
    print("airport clerk thinks you're an airport employee and they ask you to take out pile of trash")

    answer = input("Do you want to help? (Y/N): ").lower()

    if answer == "y":
        print("You take out the trash and the clerk thanks you for your help. You lose one distance point but gain x amount of currency.")
    elif answer == "n":
        print("the clerk becomes suspicious of you and wants to talk to you for a very long time before letting you continue your journey. you lose 2 distance points")
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
                currency -= x
                print("One thing changed!")
                return  #Lopetetaan suoritus, kun yksi muutos on tehty.
            else:
                print("You don't have enough money to change one thing.")
        elif choice == "2":
            if currency >= 2 * x:
                currency -= 2 * x
                print("Two things changed!")
                return  #Lopetetaan suoritus, kun kaksi muutosta on tehty.
            else:
                print("You don't have enough money to change two things.")
        elif choice == "3":
            if currency >= y:
                currency -= y
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
