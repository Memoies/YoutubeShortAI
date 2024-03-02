from YoutubeShortAI import YoutubeShortAI
from constants import *

import g4f.debug


g4f.debug.logging = DEBUG_ENABLED


def main():
    ytsai = YoutubeShortAI()
    ytsai.generateVideo("fun fact")


if __name__ == "__main__":
    main()
