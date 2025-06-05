task = input("Enter a task: ")
priority = input("Enter a priority (high ,medium ,low)")
bound = input("is it time bounded (yes or no)")

match priority:
    case "high":
        if bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Complete it when possible.")
    case "low":
        if bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it still needs to be done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
