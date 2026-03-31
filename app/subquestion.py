import re

from app.config import get_llm
from app.prompts import subquestion_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger
from app.utils.streaming import StreamHandler

stream_handler = StreamHandler(prefix="\n")
llm = get_llm(stream=True, callbacks=[stream_handler])


def generate_subquestions(topic: str, stream_to_terminal: bool = True) -> list[str]:

    try:
        prompt = subquestion_prompt.format(topic=topic)
        response = llm.invoke(prompt)
        text = response.content.strip()

        matches = re.findall(r"\d\.\s*(.+?)(?=\d\.|$)", text, flags=re.DOTALL)

        if len(matches) != 3:
            logger.error(f"Expected 3 subquestions, got {len(matches)} -> {matches}")
            raise (
                CustomException(
                    f"Expected 3 subquestions, got {len(matches)} -> {matches}"
                )
            )

        questions = [q.strip().replace("\n", " ") for q in matches]

        logger.info(f"Sub-questions generated successfully: {questions}")
        return questions

    except Exception as e:
        logger.error("Failed to generate subquestion")
        raise CustomException(e)


if __name__ == "__main__":
    topic = "Global warming"
    questions = generate_subquestions(topic)
    print(questions)
