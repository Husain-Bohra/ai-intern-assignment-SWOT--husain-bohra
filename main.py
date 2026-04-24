import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_groq(question: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def main():
    print("Ask Groq anything. Type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() == "exit":
            print("Goodbye!")
            break
        print("\nGroq:", ask_groq(question), "\n")

if __name__ == "__main__":
    main()