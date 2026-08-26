def greet_student(name):
    print(f"Hello, {name}!")


def calculate_weekly_minutes(minutes_per_day, days_per_week):
    total_minutes = minutes_per_day * days_per_week
    return total_minutes

def convert_to_hours(minutes):
    return minutes / 60

def create_study_msg(topic,days_per_week):
    print(f"I will study {topic} for {days_per_week}")

def determine_pace(minutes_per_day):
    if minutes_per_day >= 60:
        return "intensive"
    elif minutes_per_day >= 30:
        return "steady"
    else:
        return "light"


name = input("What is your name? ")

try:
    minutes_per_day = int(
        input("How many minutes will you study each day? ")
    )
    days_per_week = int(
        input("How many days per week will you study? ")
    )
    topic = input("What do you want to learn? ")
    if minutes_per_day <= 0:
        print("Minutes must be greater than 0.")

    elif days_per_week < 1 or days_per_week > 7:
        print("Days must be between 1 and 7.")

    else:
        weekly_minutes = calculate_weekly_minutes(
            minutes_per_day,
            days_per_week
        )

        learning_pace = determine_pace(minutes_per_day)
        weekly_hours = convert_to_hours(weekly_minutes)

        greet_student(name)

        print(f"Weekly study time: {weekly_minutes} minutes")
        print(f"Weekly study hours: {weekly_hours:.1f}")
        print(f"I will learn {topic} for {days_per_week} days")
        print(f"Learning pace: {learning_pace}")

except ValueError:
    print("Invalid input. Please enter whole numbers.")