import connection
from connection import connect
import time
import uuid
from colorama import Fore

def start(screen_name): #annetaan inputina saatu pelaajan nimi

    def generate_player_id():
        return str(uuid.uuid4()) # Käytetään uuid4() komentoa uuid-kirjastosta. Generoi turvallisen ID:n

    mycursor = connect.cursor()
    sql = f"INSERT INTO game (id, location, screen_name, currency, alien_distance, in_possession) VALUES (%s, %s, %s, %s, %s,%s)"
    mycursor.execute(sql, (generate_player_id(), 'MUHA', screen_name, 140, 6, False))  # Annetaan sql lauseessa annettuihin kolumneihin halutut arvot
    # MUHA = José Martí International Airport
    mycursor.fetchall()

    print("Great! Now let's start...")

    speed = 0.03 # Nopeus lore-tekstille

    lore = Fore.RED + '''
    It's the year 2586, and humanity has developed its technology to the highest
    level, overcoming a long battle against climate change. Life thrives in harmony
    as all countries have banned and ultimately forgotten environmentally harmful 
    energy sources, replaced by eco-friendly alternatives championed by top advocates. 
    However, Earth now faces an even darker fate as evil aliens suddenly arrive. 
    These terrifying aliens come with the intention of conquering the world and 
    annihilating humanity. They threaten to unleash a deadly virus designed to wipe
    out mankind.

    You are part of a resistance movement whose goal is to prevent the aliens 
    intentions and save humanity from destruction. Together with top scientists, 
    you have developed an antidote to the aliens deadly virus in a secret laboratory
    near Jose Marti International Airport in Cuba. However, creating the antidote 
    requires an ancient ingredient. According to the laboratory's lead scientist 
    Alex Zen, ingredient is found only in a super laboratory, located in an extremely 
    secretive location near Oslo Airport in Norway.

    You have been chosen for the mission to retrieve this ingredient from Norway 
    and safely transport it back to the resistance headquarters in Cuba, 
    where the antidote can be manufactured. Your journey won't be easy. 
    The aliens are intelligent they know about your plan regarding the antibody. 
    They also have garnered supporters among humanity who are not keen on the 
    resistance's plans and want to prevent your actions. You must take a circuitous 
    route, overcome various challenges and deceive the aliens and their supporters 
    along the way to succeed in your mission and save humanity from destruction. 
    The fate of the world is in your hands. Good luck!
    '''
    for letter in lore: # kirjain kerrallaan
        print(letter, end='', flush=True) # end: estää uuden rivin tulostamisen jokaisen kirjaimen jälkeen, flush: pakottaa tulostuksen heti eli näkyy välittömästi ilman puskurointia
        time.sleep(speed) # Aiheuttaa lyhyen viiveen jokaisen kirjaimen tulostuksen jälkeen, muuttujalle annettu arvo ylempänä
    print()
