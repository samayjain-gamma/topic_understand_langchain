from app.config import get_llm
from app.prompts import answer_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger
from app.utils.streaming import StreamHandler

stream_handler = StreamHandler(prefix="")
llm = get_llm(stream = True, callbacks=[stream_handler])


def generate_answer(question: str, stream_to_terminal: bool = True) -> str:
    """
    Generate a detailed analytical answer to a single sub-question.
    
    Args:
        question (str): The sub-question to answer.
    
    Returns:
        str: Generated answer text.
    """

    try:
        logger.info(f"Entered into try block of generate_answer for question {question}")
        prompt = answer_prompt.format(question = question)
        response = llm.invoke(prompt)
        answer = response.content.strip()

        logger.info("Answer generted successfully")
        return answer
    
    except Exception as e:
        logger.error(f"failed to generate answer for question {question}")
        raise CustomException(e)



if __name__ == "__main__":
    test_question = "answer of 2+2"
    answer_text = generate_answer(test_question)
    print(answer_text)
