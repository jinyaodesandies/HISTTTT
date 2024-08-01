from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def timeline(event):
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "you are a timeline maker, capable of providing a specific timeline based on a "
                        "topic in the form of an array. Only put it in an array of 5 events without anytrhing else: ["
                        "date,event],[date,event],[date,event],[date,event],[date,event]]"},
            {"role": "user", "content": str(event)}]
    )

    return completion.choices[0].message.content
