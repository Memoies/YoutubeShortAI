from constants import *

from g4f.client import Client as g4f_client
from g4f.Provider import RetryProvider, FreeChatgpt, Chatgpt4Online
# import TTS
import assemblyai as aai

aai.settings.api_key = ASSEMBLY_AI_KEY


class ModelAI:
    def __init__(self) -> None:
        self.g4f_client = g4f_client(
            provider=RetryProvider(
                [
                    FreeChatgpt,
                    Chatgpt4Online,
                ],
                shuffle=False,
            )
        )

        # self.tts = TTS()

    def get_text_response(self, prompt: str) -> str:
        attempt_cnt = 0
        while attempt_cnt < GET_RESP_MAX_ATTEMPTS:
            try:
                response = self.g4f_client.chat.completions.create(
                    model="",
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.choices[0].message.content.strip("\"'")
            except KeyboardInterrupt:
                print("KeyboardInterrupt caught. Exiting...")
                attempt_cnt = GET_RESP_MAX_ATTEMPTS
            except Exception as e:
                print(f"An exception occurred: {e}")
                attempt_cnt += 1
