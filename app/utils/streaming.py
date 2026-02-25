from langchain_core.callbacks import BaseCallbackHandler
from app.utils.logger import logger 
from app.utils.exception import CustomException

import re

class StreamHandler(BaseCallbackHandler):
    """
    Reusable streaming handler for print LLM output in streams, token by token.
    """
    
    def __init__(self, prefix: str = ""):
        """
        Args:
            prefix (str): Optional text to prefix each token line (e.g., "Answer: ")
        """
        self.prefix = prefix
        self.buffer = ""
        self.sentence_pattern = re.compile(r'(.+?[.!?])(\s|$)')



    def on_llm_new_token(self, token: str, **kwargs) -> None:
        """
        Accumulate tokens and print only full sentences.
        """
        try:
            self.buffer += token

            while True:
                match = self.sentence_pattern.search(self.buffer)
                if not match:
                    break

                sentence = match.group(1).strip()

                print(f"{self.prefix}{sentence} ", end="", flush=True)

                self.buffer = self.buffer[match.end():]

        except Exception as e:
            logger.error(f"error during streaming occured")
            raise CustomException(e)


    def on_llm_end(self, response, **kwargs) -> None:
        """
        Called when LLM finishes.
        Optionally flush remaining buffer if it forms a valid sentence.
        """
        self.buffer = ""

        print("\n", flush=True)
        logger.info("Streaming finished.")        
