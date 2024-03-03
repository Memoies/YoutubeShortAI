from constants import *
from ModelAI import ModelAI
import json


class YoutubeShortAI:
    def __init__(self) -> None:
        self.modelai = ModelAI()

    def generate_topic(self, niche: str = "") -> str:
        if niche == "":
            req_prompt = f"Give me a random specific idea for Youtube Short video."
        else:
            req_prompt = f'Give me a specific idea for Youtube Short video about this topic: "{niche}".'
        condition_prompt = "The topic must be specific. Only answer me the topic, nothing else."
        return self.modelai.generate_response(" ".join([req_prompt, condition_prompt]))

    def generate_title(self, subject: str = "") -> str:
        if subject == "":
            req_prompt = f"Give me a random Youtube Short title including hashtag."
        else:
            req_prompt = f'Give me a Youtube Short title including hashtag for this subject: "{subject}".'
        condition_prompt = "Only answer me the title, nothing else. The answer must be a string with maximum 50 characters."
        return self.modelai.generate_response(" ".join([req_prompt, condition_prompt]))

    def generate_description(self, title: str) -> str:
        req_prompt = f'Give me a description for this Youtube Short title: "{title}".'
        condition_prompt = "Only answer me the description, nothing else."
        return self.modelai.generate_response(" ".join([req_prompt, condition_prompt]))

    def generate_image(self, prompt: str) -> str:
        image_models = [
            # "v1",
            # "v2",
            "v3",
            "lexica",
            "prodia",
            "simurg",
            "animefy",
            "raava",
            "shonin",
        ]

        for i in image_models:
            self.modelai.generate_image(prompt, i)
        # return self.modelai.generate_image(prompt)

    def generate_video(self, niche: str = ""):
        subject = self.generate_topic(niche)
        title = self.generate_title(subject)
        description = self.generate_description(title)
        metadata = {
            "topic": subject,
            "title": title,
            "description": description,
        }
        print(json.dumps(metadata, indent=4))
