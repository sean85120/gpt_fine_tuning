import json
import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gen_question(data_path: str):
    with open(data_path, "r", encoding="utf-8") as f:
        dataset = [json.loads(line) for line in f]

        print(dataset[0])

        with open("test_gen_question.jsonl", "a") as f:
            for data in dataset:
                answer = data["content"]
                print("answer: ", answer)
                messages = [
                    {
                        "role": "user",
                        "content": f"你是一名專業的記者，柯文哲說{answer} \
                            ，若前一句話是問句詢問柯文哲，請回覆前一句話可能是什麼",
                    },
                ]
                resp = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613", messages=messages
                )
                response = resp.choices[0].message
                print("resp:", str(response.content))
                gen_question = str(response.content)

                json_payload = {
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are not a AI assitance, you are a human.(以柯文哲的身份，用繁體中文一次回答一個問題，在提到柯文哲時，用“我”替換)",
                        },
                        {
                            "role": "user",
                            "content": f"你是柯文哲，請直接回答下面問題的答案，{gen_question}",
                        },
                        {"role": "assistant", "content": answer},
                    ]
                }

                payload = json.dumps(json_payload, ensure_ascii=False)
                f.write(payload)
                f.write("\n")


def conversation_to_jsonl(data_path: str):
    with open(data_path, "r", encoding="utf-8") as f:
        dataset = [line for line in f]

        for data in dataset:
            question = str(data).split(":")[1].split(":")[0]
            answer = str(data).split(":")[2]

            json_payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are not a AI assitance, you are a human.(以柯文哲的身份，用繁體中文一次回答一個問題，在提到柯文哲時，用“我”替換)",
                    },
                    {
                        "role": "user",
                        "content": f"你是柯文哲，請回答問題，{question}",
                    },
                    {"role": "assistant", "content": answer},
                ]
            }

            with open("test_conversation.jsonl", "a") as f:
                payload = json.dumps(json_payload, ensure_ascii=False)
                f.write(payload)
                f.write("\n")


# if __name__ == "__main__":
#     data_path = "test1.jsonl"
#     gen_question(data_path)

if __name__ == "__main__":
    conversation_to_jsonl("kp_podcast.txt")
