import re

from langchain_core.callbacks import BaseCallbackHandler

from app.utils.exception import CustomException
from app.utils.logger import logger


class StreamHandler(BaseCallbackHandler):

    def __init__(self, prefix: str = ""):

        self.prefix = prefix
        self.buffer = ""
        self.sentence_pattern = re.compile(r"(.+?[.!?])(\s|$)")

    def on_llm_new_token(self, token: str, **kwargs) -> None:

        try:
            self.buffer += token

            while True:
                match = self.sentence_pattern.search(self.buffer)
                if not match:
                    break

                sentence = match.group(1).strip()

                print(f"{self.prefix}{sentence} ", end="", flush=True)

                self.buffer = self.buffer[match.end() :]

        except Exception as e:
            logger.error("error during streaming occured")
            raise CustomException(e)

    def on_llm_end(self, response, **kwargs) -> None:

        self.buffer = ""

        print("\n", flush=True)
        logger.info("Streaming finished.")
