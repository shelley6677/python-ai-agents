# student = {
#     "name": "Shelley",
#     "topic": "Python",
#     "minutes_per_day": 30,
#     "days_per_week": 4
# }
# student["topic"]="AI Agents"
# student["level"]="Beginner"

# print(student.get("name"))
# print(student.get("email","Email not provided"))
# print(student["name"])
# print(student["topic"])

# def calculate_weekly_minutes(profile):
#     return profile["minutes_per_day"] * profile["days_per_week"]


# name = input("What is your name? ")
# topic = input("What do you want to learn? ")

# try:
#     minutes_per_day = int(
#         input("How many minutes will you study each day? ")
#     )
#     days_per_week = int(
#         input("How many days per week will you study? ")
#     )

#     if minutes_per_day <= 0:
#         print("Minutes must be greater than 0.")

#     elif days_per_week < 1 or days_per_week > 7:
#         print("Days must be between 1 and 7.")

#     else:
#         student = {
#             "name": name,
#             "topic": topic,
#             "minutes_per_day": minutes_per_day,
#             "days_per_week": days_per_week
#         }

#         weekly_minutes = calculate_weekly_minutes(student)
#         student["weekly_minutes"] = weekly_minutes

#         print("\n--- Student Profile ---")

#         for key, value in student.items():
#             print(f"{key}: {value}")

# except ValueError:
#     print("Invalid input. Please enter whole numbers.")

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

    elif days_per_week < 1 or days_per_week > 7:
        print("Days must be between 1 and 7.")

    else:
        student = {
            "name": name,
            "topic": topic,
            "minutes_per_day": minutes_per_day,
            "days_per_week": days_per_week,
            "is_beginner": True
        }
    def create_summary(profile):
        return (
        f"{profile['name']} will study for {profile['topic']} "
        f"for {profile['minutes_per_day']} minutes, {profile['days_per_week']} days each week "
        )
    summary=create_summary(student)
    print(f"\n{summary}")  
except ValueError:
    print("Invalid input. Please enter whole numbers.")