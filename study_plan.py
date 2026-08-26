name = input("What is your name? ")
topic = input("What do you want to learn? ")

try:
    minutes_per_day = int(input("How many minutes can you study each day? "))
    days_per_week = float(input("How many days per weeks you intent to study? "))

    if minutes_per_day <0:
        print("Minutes must be greater than 0")
    
    elif days_per_week < 1 or days_per_week > 7:
        print("Days must be entered between 1 and 7")
    else:
        minutes_per_week = minutes_per_day * days_per_week
        hours_per_week = minutes_per_week / 60


        if minutes_per_day >= 60:
            pace = "intensive"
        elif minutes_per_day >= 30:
            pace = "steady"
        else:
            pace = "light"

        print("\n--- Your Study Plan ---")
        print(f"Student: {name}")
        print(f"Topic: {topic}")
        print(f"Daily study time: {minutes_per_day} minutes")
        print(f"You will study {days_per_week} days")
        print(f"Weekly study time: {minutes_per_week:g} minutes")
        print(f"Weekly study time: {hours_per_week:.1f} hours")
        print(f"Learning pace: {pace}")

except ValueError:
    print("Invalid input. Please enter numbers only.")

