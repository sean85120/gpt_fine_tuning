import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def gen_dataset(file):
    training_file = openai.File.create(file=open(file, "rb"), purpose="fine-tune")

    print("training_file:", training_file)

    return training_file["id"]


if __name__ == "__main__":
    file = "./侯友宜_dataset_gpt_1019.jsonl"
    dataset = gen_dataset(file)
