import openai
import os


class ChatGpt:
    def __init__(self) -> None:
        openai.api_key = os.environ["OPENAI_API_KEY"]

    def generate_single_input_text(self, input: str):
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": input,
                }
            ],
            temperature=0.7,
            # max_tokens=4097,
            n=1,
            stop=None,
        )
