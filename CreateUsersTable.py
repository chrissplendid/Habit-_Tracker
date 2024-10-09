import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Chibuike",
    password="900101@Chris",
    database="HabitTrackerDatabase"
)

dbcursor = db.cursor()
dbcursor.execute("CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(255), Age VARCHAR(255), Password VARCHAR(255), Date, UserStatus VARCHAR(255))")