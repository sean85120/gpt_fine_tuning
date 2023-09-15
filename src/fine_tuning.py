import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# 1 estimate cost: 6.27948 usd with 261645 tokens * 3 epochs ( default )
# 2 estimate cost: 3.65383 usd with 152243 tokens * 3 epochs ( default )
def fine_tuning(training_file_id):
    fine_tuned_model = openai.FineTuningJob.create(
        training_file=training_file_id, model="gpt-3.5-turbo"
    )

    return fine_tuned_model


def fine_tuning_status(model):
    fine_tuning_job = openai.FineTuningJob.retrieve(model)

    return fine_tuning_job


def list_fine_tuning():
    fine_tuned_list = openai.FineTuningJob.list()

    return fine_tuned_list


# if __name__ == "__main__":
#     training_file_id = "file-cKSb4uTMcO0NHvqkjT2e30tC"
#     model = fine_tuning(training_file_id=training_file_id)
#     print("fine_tune_model:", model)

if __name__ == "__main__":
    model = "ftjob-Q2NWWTrQKe95DkLVdeEwvl2q"
    fine_tuning_job = fine_tuning_status(model=model)
    print("fine_tuning_job_status:", fine_tuning_job)
