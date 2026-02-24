from app.config import get_llm
from app.prompts import evaluator_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger

llm = get_llm()


def evaluate_answer(question: str, answer: str) -> str:
    """
    Evaluate a generated answer for a sub-question

    Args:
        question (str): The sub-question text.
        answer (str): The generated answer to evaluate.

    Returns:
        str: "PASS" or "FAIL"
    """

    try:
        prompt = evaluator_prompt.format(question = question, answer= answer)
        response = llm.invoke(prompt)
        verdict = response.content.strip().upper()

        if verdict not in ["PASS", "FAIL"]:
            logger.warning(f"Unexpected evaluator output: {verdict}. Defaulting to FAIL.")
            verdict = "FAIL"

        logger.info(f"Evaluation for question '{question}': {verdict}")
        return verdict


    except Exception as e:
        logger.error(f"Failed to evaluate answer for question: {question}")
        raise CustomException(e)


if __name__ == "__main__":
    test_question = "How do rising temperatures and extreme weather events affect crop productivity?"
    test_answer = "Cricket is a game of sportsman spirit, it does not allow anyone from any background to come and play. Hope in the next worldcup, india wins the toss in all games."
    
    verdict = evaluate_answer(test_question, test_answer)
    print(f"Verdict: {verdict}")