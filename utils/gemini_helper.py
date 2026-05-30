from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(model, prompt):

    retries = 3

    for i in range(retries):

        try:

            response = client.models.generate_content(

                model=model,

                contents=prompt

            )

            return response.text

        except Exception as e:

            error = str(e)

            if "503" in error:

                time.sleep(5)

            else:

                return f"Error: {error}"

    return "Gemini servers are busy right now. Try again later."