# Get user inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Start with an empty base message
base_message = ""

# Match case based on priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unspecified priority"

# Add urgency based on time sensitivity
if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    base_message += ". Consider completing it when you have free time."

# Final output 
print(f"Reminder: {base_message}")

