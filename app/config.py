import os

from langchain_ollama import ChatOllama

from app.utils.exception import CustomException
from app.utils.logger import logger


def get_llm(stream: bool = False, callbacks=None):
    """
    Initialize and return the instance of Ollama LLm model
    Model -> phi
    """

    try:
        model_name = os.getenv("OLLAMA_MODEL", "phi")

        llm = ChatOllama(
            model=model_name,
            temperature=0.2,
            num_predict=512,
            streaming=stream,
            callbacks=callbacks,
        )

        logger.info(f"LLM initialized successfully with modekl {model_name}")

        return llm

    except Exception as e:
        logger.error("Failed to initialize LLM")
        raise CustomException(e)


if __name__ == "__main__":
    llm = get_llm()
    response = llm.invoke("HEllo")
    print(response.content)
