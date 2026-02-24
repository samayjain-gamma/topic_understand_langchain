
Topic Understanding project
using langchain

The Problem: Given a topic (e.g. "climate change impact on agriculture"), the system should:

Break the topic into 3 sub-questions automatically
Answer each sub-question using a different "agent"
Combine all answers into a final summarized report
If any answer is too vague or short, it should loop back and retry that specific sub-question — max 2 retries


Everything runs in the terminal. Input is a string. Output is a printed report.



----------------------------