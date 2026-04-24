# AI Intern Assignment — SWOT Software

This was built as part of the screening assignment for the AI Intern role at SWOT Software.

## What it does

A simple conversational script that takes your question as input, sends it to Groq's LLM API, and prints the response back to you. It runs in a loop so you can keep asking questions until you type `exit`.

## Why Groq?

Groq offers a genuinely free API with no credit card required, and it runs open source models like Llama 3.3 extremely fast. It was the most practical choice for a lightweight assignment like this.

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/Husain-Bohra/ai-intern-assignment-SWOT--husain-bohra.git
cd ai-intern-assignment-SWOT--husain-bohra
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Get a Groq API key**

Go to [console.groq.com](https://console.groq.com), create a free account, and generate an API key.

**4. Create a `.env` file in the project folder**

```
GROQ_API_KEY=your_api_key_here
```

**5. Run the script**

```bash
python main.py
```

## Usage

```
Ask Groq anything. Type 'exit' to quit.

You: What is machine learning?
Groq: Machine learning is a branch of AI that enables systems to learn from data...

You: exit
Goodbye!
```

— Husain Bohra