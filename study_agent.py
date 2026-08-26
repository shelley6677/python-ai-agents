class StudyAgent:
    def __init__(self, name):
        self.name = name
        self.completed_tasks = []

    def introduce(self):
        return (
            f"Hello! I am {self.name}, your study agent.\n"
            "Commands: plan, complete, progress, motivate, help, quit"
        )

    def create_plan(self):
        topic = input("What topic will you study? ")

        try:
            minutes = int(input("How many minutes? "))

            if minutes <= 0:
                return "Minutes must be greater than 0."

            return f"Study {topic} for {minutes} minutes."

        except ValueError:
            return "Please enter a whole number for minutes."

    def complete_task(self):
        task = input("Which task did you complete? ").strip()

        if not task:
            return "The task cannot be empty."

        self.completed_tasks.append(task)
        return f"Completed: {task}"

    def show_progress(self):
        if not self.completed_tasks:
            return "You have not completed any tasks yet."

        message = "\n--- Completed Tasks ---"

        for number, task in enumerate(
            self.completed_tasks,
            start=1
        ):
            message += f"\n{number}. {task}"

        return message

    def motivate(self):
        return "Small, consistent progress leads to big results!"

    def respond(self, command):
        command = command.lower().strip()

        if command == "plan":
            return self.create_plan()
        elif command == "complete":
            return self.complete_task()
        elif command == "progress":
            return self.show_progress()
        elif command == "help":
            return "Commands: plan, complete, progress, motivate, help, quit"
        elif command == "motivate":
            return self.motivate()           
        else:
            return "I do not understand that command."


