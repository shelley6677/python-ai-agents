topics = ["Python basics", "Git and GitHub", "AI agents","Docker"]

try:
    minutes_per_day = int(
        input("How many minutes will you study each day? ")
    )
    days_per_week = int(
        input("How many days per week will you study? ")
    )

    if minutes_per_day <= 0:
        print("Minutes per day must be greater than 0.")

    elif days_per_week < 1 or days_per_week > 7:
        print("Days per week must be between 1 and 7.")

    else:
        
        # schedule = []
        # for topic in topics:
        #     print(f"I will learn {topic}")
        topics.append("Testing")
        for number, topic in enumerate(topics,start=1):
            print(f"Day {number} : Study {topic} for {minutes_per_day} minutes")
        # for day_number in range(1, days_per_week + 1):
        #     study_session = (
        #         f"Day {day_number}: Study {topic} "
        #         f"for {minutes_per_day} minutes"
        #     )
        #     schedule.append(study_session)

        total_minutes = minutes_per_day * days_per_week

        print("\n--- Weekly Schedule ---")

        # for session in schedule:
        #     print(session)

        print(f"\nTotal study time: {total_minutes} minutes")

except ValueError:
    print("Invalid input. Please enter whole numbers.")