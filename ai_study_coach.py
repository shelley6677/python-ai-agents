import os

from pathlib import Path
from dotenv import load_dotenv
from openai import APIStatusError, OpenAI, OpenAIError


env_file = Path(__file__).with_name(".env")

load_dotenv(dotenv_path=env_file, override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY was not found in the .env file.")
    raise SystemExit

client = OpenAI()


def ask_ai(question):
    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            instructions=(
                "You are a friendly Python tutor for a beginner. "
                "Explain concepts clearly, use short examples, "
                "and end with one small practice exercise."
            ),
            input=question
        )

        return response.output_text
    except APIStatusError as error:
        organization = error.response.headers.get(
            "openai-organization",
            "Not provided"
        )

        print(f"Request ID: {error.request_id}")
        print(f"Organization used: {organization}")

        return f"API error: {error}"

    except OpenAIError as error:
        return f"API error: {error}"
    


print("AI Study Coach")
print("Ask a Python question, or type 'quit' to stop.")

while True:
    user_question = input("\nYou: ").strip()

    if user_question.lower() in ["quit", "exit", "stop"]:
        print("Coach: Keep practicing. Goodbye!")
        break

    if not user_question:
        print("Coach: Please enter a question.")
        continue

    answer = ask_ai(user_question)
    print(f"\nCoach: {answer}")