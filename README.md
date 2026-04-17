# Conversational-Chatbot
A rule-based conversational agent built in Python that handles multi-turn dialogue using structured intent matching and response logic.
 
What it does
 
The chatbot takes user input, identifies the intent behind it, and maps it to an appropriate response â€” handling a range of conversation flows and edge cases without relying on a language model.
 
Building it required thinking carefully about user experience at the language level: how should a system respond when input is ambiguous? What makes a reply feel natural rather than robotic? How do you structure a conversation so it doesn't dead-end?
 
These are design questions as much as engineering ones, and working through them gave me an early appreciation for how much thought goes into the interaction layer of any product.
 
How it works
 
- Parses user input and matches it against a defined set of intents
- Uses a pattern-response architecture to generate context-appropriate replies
- Handles fallback states gracefully when input doesn't match any known intent
- Designed to be easily extensible, new intents and responses can be added without restructuring the core logic
 
Tech
 
- Python
- Rule-based NLP (pattern matching, intent classification)
- Git for version control
 
What I learnt
 
This project was a hands-on introduction to the idea that good systems are designed for the people using them, not just for technical correctness. A response can be functionally accurate but still feel wrong. Getting that right is a design problem.
 
It also sparked a broader interest in how AI and language can be used to create experiences that feel genuinely useful which continues to shape the kind of work I want to do.
 