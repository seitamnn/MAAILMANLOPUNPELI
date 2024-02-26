# tääl vaa tehää yhteys -> ku halutaan käyttää toises tiedostos nii laitetaa import connection
import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)