import mysql.connector
import datetime

#Establish A Connection to the Database
db = mysql.connector.connect(
    host="localhost",
    user="Chibuike",
    password="900101@Chris",
    database="HabitTrackerDatabase"
)

#Validate User
Username = "Chibuike"

#Create a class named MyHabits
class MyHabits:
    #Define the name, period, date and status properties for the class
    def __init__(self, username, habitName, habitPeriod, startDate, habitStatus):

        self.username = username
        self.habitName = habitName
        self.habitPeriod = habitPeriod
        self.startDate = startDate
        self.habitStatus = habitStatus

        print("ENTER 1 TO CREATE A NEW HABIT")
        print("ENTER 2 TO VIEW HABITS")
        print("ENTER 3 TO VIEW TODAY'S TASK(S)")
        print("ENTER 4 TO VIEW WEEKLY TASK(S)")
        GoTo = input("PLEASE ENTER A DIGIT BETWEEN 1 - 4: ")

        if GoTo == 1:
            #CREATE A NEW HABIT
            #Create an object called habitEntry and provide it with the property values
            habitEntry = MyHabits(Username, input("Enter A Habit: "), "Daily", datetime.datetime.now(), "Active")
            #Print the User's Name
            print("Username: " + habitEntry.username)
            #Print the Habit Name
            print("Habit: " + habitEntry.habitName)
            #Print the Habit Period
            print("Habit Period: " + habitEntry.habitPeriod)
            #Print the Habit Entry Date
            print("Date: " + f"{habitEntry.startDate}")
            #Print the Habit Status
            print("Habit Status: " + habitEntry.habitStatus)
            #Insert the Habit into the Habits Table in the Database
            dbcursor = db.cursor()
            query = "INSERT INTO Habits (Username, HabitName, HabitPeriodicity, Date, Habitstatus) VALUES (%s, %s, %s, ?, %s)"
            queryValues = (self.username, self.habitName, self.habitPeriod, self.startDate, self.habitStatus)
            db.commit()
            print(dbcursor.rowcount, "Habit Created.")

        elif GoTo == 2:
            #VIEW HABITS
            #Fetch the user's habits record from the Habits table
            dbcursor = db.cursor()
            query = "SELECT * FROM Habits WHERE HabitStatus = 'Active' AND Username = %s"
            user = (Username, )
            dbcursor.execute(query, user)
            habits = dbcursor.fetchall()
            #Display Habits to User
            for x in habits:
                print(x)
        elif GoTo == 3:
            #VIEW TODAY'S TASK(S)
            pass
        elif GoTo == 4:
            #VIEW WEEKLY TASK(S)
            pass
        else:
            print("INVALID COMMAND!")