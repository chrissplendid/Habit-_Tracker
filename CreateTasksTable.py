import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Chibuike",
    password="900101@Chris",
    database="HabitTrackerDatabase"
)

dbcursor = db.cursor()
dbcursor.execute("CREATE TABLE Tasks (id INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(255), Task VARCHAR(255), TaskInterval VARCHAR(255), Date, TaskStatus VARCHAR(255))")