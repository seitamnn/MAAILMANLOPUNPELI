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