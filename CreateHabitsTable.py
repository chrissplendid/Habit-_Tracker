import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Chibuike",
    password="900101@Chris",
    database="HabitTrackerDatabase"
)

dbcursor = db.cursor()
dbcursor.execute("CREATE TABLE Habits (id INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(255), HabitName VARCHAR(255), HabitPeriodicity VARCHAR(255), Date, HabitStatus VARCHAR(255))")