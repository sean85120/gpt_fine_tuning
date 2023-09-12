import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.create(file=open("mydata.jsonl", "rb"), purpose="fine-tune")

openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo")


def fine_tuning():
    print("test")
    pass
