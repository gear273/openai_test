import openai
import pandas
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {"role": "user", "content": "Explain how to assemble a PC"}
    ],
    functions=[
        {
            "name": "get_answer_for_user_query",
            "description": "Get user answer in series of steps",
            "parameters": {
                'title': 'StepByStepAIResponse',
                'type': 'object',
                'properties': {'title': {'title': 'Title', 'type': 'string'},
                               'steps': {'title': 'Steps', 'type': 'array', 'items': {'type': 'string'}}},
                'required': ['title', 'steps']
            }
        }
    ],
    function_call={"name": "get_answer_for_user_query"}
)

print(response)
