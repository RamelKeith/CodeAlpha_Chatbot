# CodeAlpha_Chatbot

A rule-based conversational chatbot built in Python as part of the CodeAlpha Python Programming Internship.

---

## 🚀 Features
- **Predefined Response Engine**: Evaluates user input strings to deliver contextual, rule-based replies.
- **Continuous Interaction Loop**: Operates via a robust `while` loop that listens for input until an exit command is provided.
- **Clean Exit Handling**: Gracefully terminates the session upon receiving trigger words like `goodbye`, `bye`, or `exit`.

## 🛠️ Key Concepts Used
- String normalization (`lower().strip()`)
- Conditional control flow (`if-elif-else`)
- Modular function architecture separating response logic from the CLI loop

## 📂 Project Structure
```text
CodeAlpha_Chatbot/
├── chatbot.py
└── README.md
