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