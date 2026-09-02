habits = []
logs = []
print("Welcome to Habit Tracker. What would you like to do today?")

while True:
    print(
        "Options:\n" \
        "Enter 'h' to enter a habit\n" \
        "Enter 'l' to enter a log\n" \
        "Enter 'v' to view habits\n" 
        "Enter 'quit' to exit: ")
    userChoice = input("Enter: ")
    print()

    if userChoice == "h":
        print("What habit would you like to start?")
        userHabitName = input("Enter: ")
        print()
        print("How long would you like to track this habit? (enter number in days)")
        userHabitDuration = int(input("Enter: "))
        logs.append([userHabitName, 0, userHabitDuration])
        print("Habit logged\n")
    elif userChoice == "l":
        print("What habit would you like to log?")
        habitToLog = input("Enter: ")
        for x in range(len(logs)):
            logEntry = logs[x]
            if habitToLog == logEntry[0]:
                logEntry[1] += 1
                print(f"Logged: {logEntry[1]} out of targeted {logEntry[2]} days completed")
                if logEntry[2] == logEntry[1]:
                    print(f"You have completed your target of {logEntry[0]} for {logEntry[2]} days.")
                    print(f"Would you like to continue {logEntry[0]}")
                    userAns = input("y/n: ")
                    if userAns == "y":
                        print("How long would you like to track this habit? (enter number in days)")
                        logEntry[2] += int(input("Enter: "))
                    else:
                        logs.remove(logEntry)
    elif userChoice == "quit":
        print("Have a good day!")
        break
    elif userChoice == "v":
        for entry in logs:
            print(f"Habit: {entry[0]}\nCompleted {entry[1]} out of targeted {entry[2]} days")
            print()

