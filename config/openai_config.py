from openai import OpenAI
import os

client = OpenAI(os.getenv("OPEN_AI_KEY"))