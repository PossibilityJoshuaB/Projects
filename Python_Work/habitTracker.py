habits = []
logs = []

import sqlite3
dbConnection = sqlite3.connect("tutorial.db")
cursor = dbConnection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS habits (" \
"id INTEGER PRIMARY_KEY," \
"habit_name VARCHAR(16)," \
"habit_progress INTEGER," \
"habit_target INTEGER)")

print("Welcome to Habit Tracker. What would you like to do today?")
print()

while True:
    print(
        "Options:\n" \
        "Enter 'h' to enter a habit\n" \
        "Enter 'l' to enter a log\n" \
        "Enter 'v' to view habits\n" 
        "Enter 'quit' to exit: ")

    userChoice = input("Enter: ")
    print()
    if cursor.fetchone() != None:
        lastID = cursor.execute("SELECT id FROM habits ORDER BY id DESC").fetchone()[0]
    else:
        lastID = 0


    if userChoice == "h":
        print("What habit would you like to start?")
        userHabitName = input("Enter: ")
        print()

        print("How long would you like to track this habit? (enter number in days)")
        userHabitDuration = int(input("Enter: "))
        print()

        logs.append([userHabitName, 0, userHabitDuration])

        cursor.execute("INSERT INTO habits (habit_name, habit_progress, habit_target) " \
        "VALUES (?, ?, ?)",
        (userHabitName, 0, userHabitDuration))
        dbConnection.commit()

        print("Habit started")
        print()
    elif userChoice == "l":
        print("What habit would you like to log?")
        habitToLog = input("Enter: ")
        print()
        print("How many days have you completed of this habit since your last update?")
        daysToLog = int(input("Enter number of days: "))
        print()

        currentCompletion = cursor.execute(f"SELECT habit_progress FROM habits WHERE habit_name = ?", (habitToLog,)).fetchone()[0]
        target = cursor.execute(f"SELECT habit_target FROM habits WHERE habit_name = ?", (habitToLog,)).fetchone()[0]

        cursor.execute(f"UPDATE habits SET habit_progress = {currentCompletion + daysToLog} WHERE habit_name = ?", (habitToLog,))
        dbConnection.commit()
        print("Habit logged")
        print()

        daysLeftToTarget = target - currentCompletion
        if daysLeftToTarget == 0:
            print(f"You have completed your target of {target} days.")
            print("Would you like to continue this habit or remove it from the tracker and move on?")
            ans = input("Enter y/n: ")
            print()
            if ans == "y":
                print("How long would you like to extend your target for?")
                targetExtension = int(input("Enter number of days: "))
                print()

                cursor.execute(f"UPDATE habits SET habit_target = {target + targetExtension} WHERE habit_name = ?", (habitToLog,))
                dbConnection.commit()
            else:
                print("Congratulations on completing your goal")
                print()

                cursor.execute(f"DELETE FROM habits WHERE habit_name = ?", (habitToLog,))
        else:
            print(f"Logged: You have completed {currentCompletion} days out of your targeted {target} days.")
            print()

    elif userChoice == "quit":

        print("Have a good day!")
        print()
        break

    elif userChoice == "v":
        allHabits = cursor.execute("SELECT * FROM habits").fetchall()
        for habit in allHabits:
            print(f"Habit: {habit[1]}\nCompleted {habit[2]} out of targeted {habit[3]} days")
            print()

    elif userChoice == "delete":
        userAunthetication = input("Enter passcode for admin privileges: ")
        if userAunthetication == "MEGATR0N":
            cursor.execute("DELETE FROM habits")
            print("Table cleared")
            print()
        else:
            break
    else:
        print("Please enter a valid input")
        print()