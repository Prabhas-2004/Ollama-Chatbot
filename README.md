# Ollama Console Chatbot

A simple AI chatbot built using Python and Ollama. The chatbot runs in the terminal and uses the Qwen2 1.5B language model to generate responses to user queries.

## Features

* Interactive command-line chatbot
* Uses Ollama for local AI inference
* Lightweight and easy to set up
* No API key required
* Runs completely on your local machine

## Technologies Used

* Python
* Ollama
* Qwen2:1.5B Model

## Project Structure

```text
Ollama-Chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
```

## Prerequisites

Before running the project, make sure you have:

1. Python 3.8 or later installed
2. Ollama installed on your system
3. Qwen2:1.5B model downloaded

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ollama-chatbot.git
cd ollama-chatbot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install Ollama

Download and install Ollama from:

https://ollama.com

### Step 4: Pull the Qwen Model

```bash
ollama pull qwen2:1.5b
```

## Running the Application

Start the Ollama service and run:

```bash
python chatbot.py
```

## Example Usage

```text
You: What is Artificial Intelligence?

Bot: Artificial Intelligence (AI) is a branch of computer science that enables machines to simulate human intelligence and perform tasks such as learning, reasoning, and decision-making.

You: exit

Bot: Goodbye!
```

## Source Code

```python
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
```

## Future Enhancements

* Streamlit Web Interface
* Voice Assistant Integration
* Chat History Storage
* RAG (Retrieval-Augmented Generation)
* Multiple Model Support
* Image Generation Support

## Author

Prabhas Gundavolu

## License

This project is for learning and educational purposes.
