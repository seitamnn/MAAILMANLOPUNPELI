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