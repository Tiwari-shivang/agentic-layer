from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPEN_AI_KEY"))