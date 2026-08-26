from study_agent import StudyAgent
from messages import WELCOME_MESSAGE, GOODBYE_MESSAGE




def run_agent():
    agent = StudyAgent("Python Coach")

    print(agent.introduce())

    while True:
        user_command = input("\nYou: ").lower().strip()

        if user_command in ["quit", "exit", "stop"]:
            print("Agent: Goodbye!")
            break

        response = agent.respond(user_command)
        print(f"Agent: {response}")


if __name__ == "__main__":
    run_agent()