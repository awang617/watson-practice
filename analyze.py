# api_key = "Slv2arJiA6DWHRfUHXyWa1Gi4kJsE0FUuaSf2lFnkLCb"
# url = "https://gateway.watsonplatform.net/natural-language-understanding/api"

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / 'ibm-credentials.env'
load_dotenv(dotenv_path=env_path)

import os
API_KEY = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_IAM_APIKEY")
URL = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_URL")

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey=API_KEY,
    url=URL
)

response = natural_language_understanding.analyze(
    html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
    features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

print(json.dumps(response, indent=2))
