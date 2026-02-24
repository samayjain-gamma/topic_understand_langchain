# from langchain.callbacks.base import BaseCallbackHandler

# class StreamHandler(BaseCallbackHandler):
#     """
#     Print tokens as they arrive from the LLM.
#     """

#     def on_llm_new_token(self, token: str, **kwargs) -> None:
#         print(token, end="", flush=True)