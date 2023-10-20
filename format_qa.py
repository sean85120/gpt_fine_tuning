import json


def format_qa(data_path: str):
    character_name = data_path.split("_")[0]

    with open(data_path, "r") as file:
        for line in file:
            data = json.loads(line)
            prompt = (data["prompt"],)
            response = data["response"]

            with open(f"{character_name}_openai_format.jsonl", "a") as f:
                json_format = {
                    "messages": [
                        {
                            "role": "system",
                            "content": f"You are not a AI assistant, you are a human.(以{character_name}的身份，\
                            用繁體中文一次回答一個問題，在提到{character_name}時，用“我”替換)",
                        },
                        {"role": "user", "content": f"你是{character_name} {prompt}"},
                        {"role": "assistant", "content": response},
                    ]
                }

                json.dump(json_format, f, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    data_path = "郭台銘_dataset_gpt_1019.jsonl"
    format_qa(data_path)

    print("Done!")
