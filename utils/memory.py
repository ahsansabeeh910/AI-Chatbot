import json
import os

FILE = "data/chat_history.json"

def load_chat():

    if not os.path.exists(FILE):

        return []

    try:

        with open(FILE,"r") as f:

            content = f.read().strip()

            if not content:

                return []

            return json.loads(content)

    except:

        return []

def save_chat(messages):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(FILE,"w") as f:

        json.dump(
            messages,
            f,
            indent=4
        )