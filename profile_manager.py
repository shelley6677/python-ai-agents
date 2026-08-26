import json

def create_profile():
    name = input("What is your name? ")
    topic = input("What do you want to learn? ")

    try:
        minutes_per_day = int(
            input("How many minutes will you study each day? ")
        )
        days_per_week = int(
            input("How many days per week will you study? ")
        )

        if minutes_per_day <= 0:
            print("Minutes must be greater than 0.")
            return None

        if days_per_week < 1 or days_per_week > 7:
            print("Days must be between 1 and 7.")
            return None

        return {
            "name": name,
            "topic": topic,
            "minutes_per_day": minutes_per_day,
            "days_per_week": days_per_week,
            "weekly_minutes": minutes_per_day * days_per_week,
            "completed_lessons": [
                "Variables",
                "Conditions",
                "Lists and loops",
                "Functions",
                "Dictionaries"
            ]
        }

    except ValueError:
        print("Please enter whole numbers.")
        return None


def save_profile(profile):
    with open("student_profile.json", "w") as file:
        json.dump(profile, file, indent=4)

    print("Profile saved successfully.")


def load_profile():
    try:
        with open("student_profile.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("No saved profile was found.")
        return None


def display_profile(profile):
    print("\n--- Student Profile ---")

    for key, value in profile.items():
        print(f"{key}: {value}")

def completed_lessons(profile):
    print("\n--- Completed Lessons ---")
    for lesson in profile.get("completed_lessons", []):
        print(f"- {lesson}")

def add_completed_lesson(profile, lesson):
    profile["completed_lessons"].append(lesson)
    return profile

profile = create_profile()

if profile is not None:
    profile = add_completed_lesson(profile, "Files and JSON")
    save_profile(profile)

    saved_profile = load_profile()

    if saved_profile is not None:
        display_profile(saved_profile)
        completed_lessons(saved_profile)
