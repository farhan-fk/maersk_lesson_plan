# virtaul activation code for VS code (.\venv\Scripts\activate)
#Principle1: Strucyuring the prompt and Tactics to get the best out of LLMs

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

OpenAI.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# def get_completion(prompt, model="gpt-4o-mini"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]

# Prompting Principle (More to follow)
# Principal1 : Write clear and specific Instructions (Not necssarily short,sometimes longer prompts give more context to LLMs to give better responses)

# Tactic 1: Use delimiters
# - Triple quotes: """
# - Triple backticks: ```
# - Triple dashes: ---
# - Angle brackets: < >
# - XML tags: <tag> </tag>

# principal 2 : Give the model time to think
# in python \ is uded to break a line into multiple lines

# text = f"""
# You should express what you want a model to do by \
# providing instructions that are as clear and \
# specific as you can possibly make them. \
# This will guide the model towards the desired output, \
# and reduce the chances of receiving irrelevant \
# or incorrect responses. Don't confuse writing a \
# clear prompt with writing a short prompt. \
# In many cases, longer prompts provide more clarity \
# and context for the model, which can lead to \
# more detailed and relevant outputs.
# """

# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """
# response = get_completion(prompt)
# print(response)

#Tactic 2: Ask for a structured output

# prompt = f"""
# Generate a list of three made-up spare parts for container ships along \
# with their manufacturers and primary use cases.
# Provide them in JSON format with the following keys:
# part_id, name, manufacturer, use_case.
# """
# # Why do we use JSON format as an output?
# # JSON is a widely-used data interchange format that is easy for both humans and machines to read and write.
# # It provides a structured way to represent data, making it ideal for scenarios where you need to exchange information between different systems or components.
# # By requesting output in JSON format, you ensure that the data can be easily parsed and processed by software applications, facilitating integration and automation.
# response = get_completion(prompt)
# print(response)

# Tactic 3: Ask the model to check whether conditions are met

# inventory = """
# {
#   "parts": [
#     {"part_id": "SP-ENG-001", "name": "Marine Diesel Filter", "stock": {"Mumbai_Warehouse": 45, "Chennai_Depot": 12}},
#     {"part_id": "SP-DEC-002", "name": "Hydraulic Pump", "stock": {"Mumbai_Warehouse": 0, "Chennai_Depot": 8}},
#     {"part_id": "SP-NAV-003",  "name": "Radar Antenna",   "stock": {"Mumbai_Warehouse": 0, "Chennai_Depot": 0}}
#   ]
# }
# """

# request_text = """
# Ship engineer needs part_id=SP-DEC-002 at Mumbai Port.
# Preferred pickup location: Mumbai_Warehouse.
# """

# prompt = f"""
# You will be provided with:
# 1) A JSON inventory database for ship spare parts
# 2) A service request

# Task:
# - If the requested part is available (stock > 0) at the preferred location, output steps for pickup.
# - If not available there but available at another location, output steps for transfer.
# - If not available anywhere, output "No stock available".

# Return your result in the format:
# Stock Status: <Available/Not Available>
# Location: <Pickup/Transfer/NA>


# --- INVENTORY JSON ---
# {inventory}

# --- SERVICE REQUEST ---
# {request_text}
# """
# response = get_completion(prompt)
# print(response)

# Tactic 4: Few shot prompting

text = f"""
Write email on container delay issue."""

prompt = f"""
Your task is to  write email in a consistent writing style.
The style is short, message-like emails (imperfect English, direct tone).

<email>:
hi sir, container stuck at customs mumbai, we submit docs last week but clearance still pending,
pls check urgent.

<email>:
sir, customer waiting since 3 days, shipment not yet departed from chennai,
vessel schedule changed, pls arrange fast tracking.

<email>:
```{text}```
"""
response = get_completion(prompt)
print(response)


#  Recap in This Lesson we learned Very Important Prompting Techniques like\
#  how we need to be specific in our instructions (Use Tactics 1), \
#  Define the structure of output (Use Tactics 2), \
#  Ask the model to verify whether certain conditions are met (Use Tactics 3),\
#  And Share Some Examples of the Desired Output (Use Tactics 4)
#  All these techniques will help you to get the best out of LLMs.
