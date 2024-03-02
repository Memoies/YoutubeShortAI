from constants import *
from ModelAI import ModelAI
import json


class YoutubeShortAI:
    def __init__(self) -> None:
        self.modelai = ModelAI()

    def getTitle(self, subject: str = "") -> str:
        if subject == "":
            req_prompt = f"Give me a random Youtube Short title."
        else:
            req_prompt = f'Give me a Youtube Short title for this subject: "{subject}".'
        condition_prompt = "Only answer me the title, nothing else. The answer must be a string with maximum 50 characters."
        return self.modelai.get_text_response(" ".join([req_prompt, condition_prompt]))

    def getDescription(self, title: str) -> str:
        req_prompt = f'Give me a description for this Youtube Short title: "{title}".'
        condition_prompt = "Only answer me the description, nothing else. The answer must be a string with maximum 200 characters."
        return self.modelai.get_text_response(" ".join([req_prompt, condition_prompt]))

    def generateVideo(self, subject: str = ""):
        title = self.getTitle(subject)
        description = self.getDescription(title)
        metadata = {
            "title": title,
            "description": description,
        }
        print(json.dumps(metadata, indent=4))
