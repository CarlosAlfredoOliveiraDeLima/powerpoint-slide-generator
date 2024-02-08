import openai, json
from pptx import Presentation

client = openai.OpenAI()

presentation_title = input("What do you want to make a presentation about? ")

query_json = """{
    "input_text": "[[QUERY]]",
    "output_format": "json",
    "json_structure": {
        "slides":"{{presentation_slides}}"
       }
    }"""

question = f"generate a 10 slide presentation for the topic {presentation_title}. Each slide should have a {{header}}, {{content}}. Return as JSON"

prompt = query_json.replace("[[QUERY]]",question)