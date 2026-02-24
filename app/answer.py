from app.config import get_llm
from app.prompts import answer_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger

llm = get_llm()


def generate_answer(question: str) -> str:
    """
    Generate a detailed analytical answer to a single sub-question.
    
    Args:
        question (str): The sub-question to answer.
    
    Returns:
        str: Generated answer text.
    """

    try:
        prompt = answer_prompt.format(question = question)
        stream_handler = Stream

        response = llm.invoke(prompt)
        answer = response.content.strip()

        logger.info("Answer generted successfully")
        return answer
    
    except Exception as e:
        logger.error(f"failed to generate answer for question {question}")
        raise CustomException(e)



if __name__ == "__main__":
    test_question = "How do rising temperatures and extreme weather events affect crop productivity?"
    answer_text = generate_answer(test_question)
    print(answer_text)