from app.config import get_llm
from app.prompts import input_guradrail_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger
from app.utils.streaming import StreamHandler

stream_handler = StreamHandler(prefix="")
llm = get_llm(stream=True, callbacks=[stream_handler])


def input_guardrail(topic: str) -> str:
    """
    Guradrail


    """
    try:
        logger.info("Entered into input gurardrail")
        prompt = input_guradrail_prompt(topic=topic)
        response = llm.invoke(prompt)

    except Exception as e:
        pass
