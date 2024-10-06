import datetime
#Create a class named MyHabits
class MyHabits:
    #Define the name, period, date and status properties for the class
    def __init__(self, habitName, habitPeriod, startDate, habitStatus):
        self.habitName = habitName
        self.habitPeriod = habitPeriod
        self.startDate = startDate
        self.habitStatus = habitStatus
#Create an object called habitEntry and provide it with the property values
habitEntry = MyHabits(input("Enter A Habit: "), "Daily", datetime.datetime.now(), "completed")
#Print the Habit Name
print("Habit: " + habitEntry.habitName)
#Print the Habit Period
print("Habit Period: " + habitEntry.habitPeriod)
#Print the Habit Entry Date
print("Date: " + f"{habitEntry.startDate}")
#Print the Habit Status
print("Habit Status: " + habitEntry.habitStatus)