import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Chibuike",
    password="900101@Chris"
)

dbcursor = db.cursor()
dbcursor.execute("CREATE DATABASE HabitTrackerDatabase")