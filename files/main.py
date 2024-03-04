# Pääohjelma tähän lol
import connection
from connection import connect
import mysql.connector
from colorama import Fore
import time
import random
from start import start

print(Fore.RED + '''
██████╗     ███████╗     █████╗      ██████╗ 
╚════██╗    ██╔════╝    ██╔══██╗    ██╔════╝ 
 █████╔╝    ███████╗    ╚█████╔╝    ███████╗ 
██╔═══╝     ╚════██║    ██╔══██╗    ██╔═══██╗
███████╗    ███████║    ╚█████╔╝    ╚██████╔╝
╚══════╝    ╚══════╝     ╚════╝      ╚═════╝ 
''')

start_choice = input("Would you like to start? (Y/N) \n").lower()
if start_choice == 'y':
    print("Welcome to our game!")
    cursor = connection.connect
else:
    print("GAME OVER")

player_name = str(input("Select a player name: \n"))
start(player_name) # start-funktio luotu start-tiedostossa

