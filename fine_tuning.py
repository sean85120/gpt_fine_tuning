import os

import openai
from dotenv import load_dotenv

from gen_dataset import gen_dataset

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# estimate cost: 6.27948 usd with 261645 tokens * 3 epochs ( default )
def fine_tuning(file):
    training_file = gen_dataset(file)

    fine_tuned_model = openai.FineTuningJob.create(
        training_file=training_file, model="gpt-3.5-turbo"
    )

    return fine_tuned_model

    # fine_tune_model: {
    #   "object": "fine_tuning.job",
    #   "id": "ftjob-eRw7CTnEWew07tNIp7zSSRTr",
    #   "model": "gpt-3.5-turbo-0613",
    #   "created_at": 1694674172,
    #   "finished_at": null,
    #   "fine_tuned_model": null,
    #   "organization_id": "org-6Kd8d957L2nX9ZTcSGSvW9Bq",
    #   "result_files": [],
    #   "status": "created",
    #   "validation_file": null,
    #   "training_file": "file-Qo2wzwjqaCunIJI1v5uEpvmO",
    #   "hyperparameters": {
    #     "n_epochs": 3
    #   },
    #   "trained_tokens": null,
    #   "error": null
    # }


def fine_tuning_status(model):
    fine_tuned_model = openai.FineTuningJob.retrieve(model)

    return fine_tuned_model


if __name__ == "__main__":
    model = "ftjob-eRw7CTnEWew07tNIp7zSSRTr"
    status = fine_tuning_status(model)
    print("fine_tune_status:", status)
