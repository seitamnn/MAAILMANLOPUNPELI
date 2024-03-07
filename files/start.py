import connection
from connection import connect
import time
import uuid


def start(screen_name): #annetaan inputina saatu pelaajan nimi

    def generate_player_id():
        return str(uuid.uuid4())

    mycursor = connect.cursor() # osotetaa tietokantaan
    sql = "INSERT INTO game (id, location, screen_name, currency, alien_distance, in_possession) VALUES (%s, %s, %s, %s, %s,%s)" #noihin laitetaa arvot jotka annetaa seuraavalla rivillä
    mycursor.execute(sql, (generate_player_id(), 'MUHA', screen_name, 1000, 100, False))  # MUHA = José Martí International Airport
    mycursor.fetchall() # palauttaa kaikki tulosjoukot, jotka vastaavat ylempään sql kyselyyn

    print("Great! Now let's start...\n")

    speed = 0.05 # nopeus tekstille

    lore = '''
    It's year 2586. Earth faces a grim fate as evil aliens suddenly arrived. 
    These terrifying aliens come to conquer the world and destroy humanity. 
    They threaten to unleash a deadly virus designed to wipe out mankind.

    You are part of a resistance movement whose goal is to prevent the aliens intentions and save humanity from destruction. 
    Together with top scientists, you have developed an antidote to the aliens deadly virus in a secret laboratory near 
    Jose Marti International Airport in Cuba. 
    However, creating the antidote requires an ancient ingredient. According to the laboratory's lead scientist 
    Alex Zen, ingredient is found only in a super laboratory, located in an extremely secretive location near 
    Oslo Airport in Norway.

    You have been chosen for the mission to retrieve this ingredient from Norway and safely transport it back to 
    the resistance headquarters in Cuba, where the antidote can be manufactured. 
    Your journey, however, will not be easy. 
    The aliens are intelligent and have learned of your plans. 
    Moreover, they have garnered supporters among humanity who are not keen on the resistance's plans and want to 
    thwart your actions. You must take a circuitous route and deceive the aliens and their supporters 
    along the way to succeed in your mission and save humanity from destruction. 
    The fate of the world is in your hands. Good luck!
    '''
    for letter in lore: # kirjain kerrallaan
        print(letter, end='', flush=True) # end: estää uuden rivin tulostamisen jokaisen kirjaimen jälkeen, flush: pakottaa tulostuksen heti eli näkyy välittömästi ilman puskurointia
        time.sleep(speed) # aiheuttaa lyhyen viiveen jokaisen kirjaimen tulostuksen jälkeen
    print()
