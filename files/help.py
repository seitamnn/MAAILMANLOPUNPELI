from connection import connect
from colorama import Fore

def help_center(screen_name, user_input):
        print(Fore.LIGHTMAGENTA_EX + 20*'-' + 'HELP CENTER' + 20*'-')
        print(Fore.BLUE + 'CURRENCY:')
        print(Fore.LIGHTMAGENTA_EX + '    How much currency do you have in your wallet\n')
        print(Fore.BLUE + 'DISTANCE:')
        print(Fore.LIGHTMAGENTA_EX + '    How many steps until the alien get u\n')
        print(Fore.BLUE + 'LOCATION:')
        print(Fore.LIGHTMAGENTA_EX + '    Where are you now our little world traveler uwu\n')
        print(Fore.BLUE + 'LORE:')
        print(Fore.LIGHTMAGENTA_EX + "    Remind me what's going on\n")
        print(Fore.LIGHTMAGENTA_EX + 51*'-')
        user_input = input(Fore.CYAN + 'Press enter to continue\n')
        help_command(screen_name, user_input)

def help_command(screen_name, input):
        if input == 'CURRENCY' or input == 'currency':
                currency_sql = f"SELECT currency FROM game WHERE screen_name='{screen_name}'"
                cursor = connect.cursor()
                cursor.execute(currency_sql)
                currency = cursor.fetchone()
                print(Fore.LIGHTMAGENTA_EX + f'\nCURRENCY: {currency[0]}\n')
        elif input == 'DISTANCE' or input == 'distance':
                distance_sql = f"SELECT alien_distance FROM game WHERE screen_name='{screen_name}'"
                cursor = connect.cursor()
                cursor.execute(distance_sql)
                distance = cursor.fetchone()
                print(Fore.LIGHTMAGENTA_EX + f'\nDISTANCE: {distance[0]} steps\n')
        elif input == 'LOCATION' or input == 'location':
                location_sql = f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE airport.ident IN(SELECT location FROM game WHERE screen_name='{screen_name}')"
                cursor = connect.cursor()
                cursor.execute(location_sql)
                location = cursor.fetchone()
                print(Fore.LIGHTMAGENTA_EX + f'\nLOCATION: {location[0]} in {location[1]}\n')
        elif input == 'lore' or input == 'LORE':
                lore = Fore.LIGHTMAGENTA_EX + '''
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
                print(lore)
        elif input == 'help' or input == 'HELP':
                help_center(screen_name, input)