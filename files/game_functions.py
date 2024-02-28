# tänne esim arpomis hommelit liikkumisee yms
import random
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
#funktio lentokentältä toiselle lentämiseen
def select_airport():
    #Yhdistetään tietokantaan
    sql = (f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country")
    cursor = connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.close()

    # Valitaan satunnaisesti kolme lentokenttää
    selected_airports = random.sample(airports, 3)

    #pelaajan check-in ja funktio antaa kolme satunnaisesti arvottua lentokenttää ja tulostaa nämä l
    print("welcome to check-in!")
    print("Choose from the following airports where you want to fly next:")
    for i in range(len(selected_airports)):
        print(f"{i + 1}. {selected_airports[i][0]} in {selected_airports[i][1]}")

    #pelaaja valitsee arvotuista lentokentistä seuraavan kohteen
    while True:
        choice = input("select next airport. Enter number between (1-3): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                break
        print("error in selection. enter number between 1-3.")

    decided_airport = selected_airports[choice - 1][0]
    print(f"your choice as the next airport is: {decided_airport}")
    return decided_airport

#Testi
chosen_airport = select_airport()
print("have a safe flight to", chosen_airport + "!")

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
    while True:
        celsius = float(input("What is the temperature in Celsius?: "))
        if celsius == 3.0:
            print("Amazing! The ingredient looks fine.")
            break
        else:
            print("Try again.")

fahrenheit_to_celsius()
