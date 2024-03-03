from constants import *

from g4f.client import Client as g4f_client
from g4f.Provider import RetryProvider, FreeChatgpt, Chatgpt4Online

# import TTS
import assemblyai as aai
import requests

aai.settings.api_key = ASSEMBLY_AI_KEY


class ModelAI:
    def __init__(self) -> None:
        self.g4f_client = g4f_client(
            provider=RetryProvider(
                [
                    Chatgpt4Online,
                    FreeChatgpt,
                ],
                shuffle=False,
            )
        )

        # self.tts = TTS()

    def generate_response(self, prompt: str) -> str:
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
                break
            except Exception as e:
                print(f"An exception occurred: {e}")
                attempt_cnt += 1

    def generate_image(self, prompt: str, image_model: str = "v3") -> str:
        attempt_cnt = 0
        while attempt_cnt < GET_RESP_MAX_ATTEMPTS:
            try:
                json = requests.get(f"https://hercai.onrender.com/{image_model}/text2image?prompt={prompt}").json()
                image_url = json["url"]
                image_path = os.path.join(ROOT_DIR, "temp", f"{image_model}.png")
                with open(image_path, "wb") as image_file:
                    # Write bytes to file
                    image_r = requests.get(image_url)
                    image_file.write(image_r.content)
                return image_path
            except KeyboardInterrupt:
                print("KeyboardInterrupt caught. Exiting...")
                break
            except Exception as e:
                print(f"An exception occurred: {e}")
                attempt_cnt += 1
