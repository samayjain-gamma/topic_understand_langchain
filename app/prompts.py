subquestion_prompt = """
You are a research planner.

Given the topic below, generate exactly 3 important, non-overlapping sub-questions required for a comprehensive and deep analysis. 

Instructions:
- Number them 1., 2., 3.
- Do not give expaination
- Do not write extra text
- Each sub-question should cover a different aspect of the topic

Topic: {topic}
"""


answer_prompt = """
Provide a detailed, structured, analytical answer to the following question:

Question: {question}

Instructions:
- Minimum 150 words
- Be specific and avoid generic statements
- Use clear structure, examples, or reasoning where possible
- Focus on answering the question directly
"""



evaluator_prompt = """
Evaluate the following answer based on these criteria:

1. Is the answer at least 150 words?
2. Is it directly relevant to the question?
3. Is it specific and analytical, not generic?

Return only one word: PASS or FAIL

Question: {question}

Answer: {answer}
"""



summary_prompt = """
Combine the following answers into a coherent final report.

Instructions:
- Include an introduction, key insights, and conclusion
- Keep it clear, structured, and concise
- Do not add content not present in the answers
- Use smooth transitions

Topic: {topic}

Sub-Questions and Answers:
{subquestions_and_answers}
"""
