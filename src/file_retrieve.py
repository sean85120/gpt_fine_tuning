import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def retrieve_file(file_id):
    file = openai.File.retrieve(file_id)

    return file


# def retrieve_file_content():
#     file_id = "file-0GH6WidWuXk9iHitZizWDJdt"
#     file = retrieve_file(file_id=file_id)

#     return file["object"]

if __name__ == "__main__":
    file_id = "file-0GH6WidWuXk9iHitZizWDJdt"
    file = retrieve_file(file_id=file_id)
    print("file:", file)
