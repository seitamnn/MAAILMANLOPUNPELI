import connection
from connection import connect
import time


def start(player_name):
    mycursor = connect.cursor()
    sql = "INSERT INTO game (id, location, screen_name, currency, alien_distance, in_possession) VALUES (%s, %s, %s, %s, %s,%s)"
    mycursor.execute(sql, (5, 'MUHA', player_name, 1000, 1000, False))  # MUHA = José Martí International Airport
    mycursor.fetchall()
    print("Great! Now let's start...\n")

    speed = 0.05

    lore = '''
    It's year 2586. Earth faces a grim fate as evil aliens suddenly arrived. 
    These terrifying aliens come to conquer the world and destroy humanity. 
    They threaten to unleash a deadly virus designed to wipe out mankind.

    You are part of a resistance movement whose goal is to prevent the aliens intentions and save humanity from destruction. 
    Together with top scientists, you have developed an antidote to the aliens' deadly virus in a laboratory in Cuba. 
    However, creating the antidote requires an ancient ingredient found only in a super laboratory in Norway.

    You have been chosen for the mission to retrieve this ingredient from Norway and safely transport it back to 
    the resistance headquarters in Cuba, where the antidote can be manufactured. 
    Your journey, however, will not be easy. 
    The aliens are intelligent and have learned of your plans. 
    Moreover, they have garnered supporters among humanity who are not keen on the resistance's plans and want to 
    thwart your actions. You must take a circuitous route and deceive the aliens and their supporters 
    along the way to succeed in your mission and save humanity from destruction. 
    The fate of the world is in your hands. Good luck!
    '''
    for letter in lore:
        print(letter, end='', flush=True)
        time.sleep(speed)
    print()