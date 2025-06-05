Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low):")
TimeBound = input("Is it time-bound? (yes/no):")

match Priority:
    case "high":
        if TimeBound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{Task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if TimeBound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{Task}' is a medium priority task. Complete it when possible.")
    case "low":
        if TimeBound == "yes":
            print(f"Reminder: '{Task}' is a low priority task, but it still needs to be done today.")
        else:
            print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
