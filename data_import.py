import os
from dotenv import load_dotenv
import requests


load_dotenv()


SESSION_COOKIE = os.getenv("SESSION_COOKIE")
cookies = {"session": SESSION_COOKIE}


def get_question_data(year, day):
    url = f"http://adventofcode.com/{year}/day/{day}/input"

    req = requests.get(
        url,
        cookies=cookies,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            + "AppleWebKit/537.36 (KHTML, like Gecko) "
            + "Chrome/120.0.0.0 Safari/537.36"
        },
        timeout=120,
    )

    response = req.text
    return response
