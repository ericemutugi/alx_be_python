# Prompts to users on tasks input
task = input("Enter your task: ")
priority = input("Priority (high, medium, low) :")
time_bound = bool(input("Is it time-bound? (yes, no): "))

match priority:
    case "high":
        print("Reminder: ", task, "is a high priority task that requires immediate attention today!")
    case "medium":
        print("Reminder: ", task, "is a medium priority task, ensure you set time to attend to it.")
    case "low":
        print("Note: ", task, "is a low priority task, plan to attend to it when you are free.")i

