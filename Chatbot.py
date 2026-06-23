from ollama import chat

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chat(
        model="qwen2:1.5b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Bot:", response["message"]["content"])