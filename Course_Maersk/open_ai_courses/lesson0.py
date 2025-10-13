
# How To connect to LLMS and Basic Prompting techniques and Interpolation

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

OpenAI.api_key  = os.getenv('OPENAI_API_KEY')
# prompt = " Tell me a joke about a cat and a dog"
# def get_completion(prompt, model="gpt-4o-mini"):
#     messages = [{"role": "user", "content": prompt}]
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0
#     )
#     return response.choices[0].message.content

# response = get_completion(prompt)
# print(response)


# # # case 1: Basic Prompting
# # prompt_basic = " Tell me a joke about a cat and a dog"

# Case 2: Passing into interpolation prompt
# user_input = "a small white dog with black spots"

# prompt = f"""
# You are given this description of a pet: "{user_input}".
# Suggest three creative names for the pet.
# Return only the names as a list.
# """
# def get_completion(prompt, model="gpt-4o-mini"):
#     messages = [{"role": "user", "content": prompt}]
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0
#     )
#     return response.choices[0].message.content

# response = get_completion(prompt)
# print(response)



religion = "Hindu"
country = "India"
gender = "girl"

# App Idea: Create an App that Suggest Baby Names based on the description of the baby religion,Country, etc..
prompt = f"""
Suggest five beautiful {gender} baby names.
The names should be popular in {country} and follow {religion} traditions.
Return only the names as a list.
"""

response = get_completion(prompt)
print(response)
