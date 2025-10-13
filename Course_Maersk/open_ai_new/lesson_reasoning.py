from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
OpenAI.api_key  = os.getenv('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI()

prompt = """
You are a port operations planner for Jawaharlal Nehru Port (JNPT), Mumbai.
There are 250 containers waiting to be loaded onto a vessel. The current loading crane can handle 30 containers per hour.
A cyclone warning has been issued, with the storm expected to hit in 7 hours and lasting for 12 hours. If the vessel doesn't depart before the cyclone, port operations will be suspended, causing a delay fee of ₹8,000 per container.
The total delay cost would be ₹20,00,000 (250 containers × ₹8,000).

Option: The port can deploy an additional mobile harbor crane at ₹1,50,000 per hour, which can load 25 containers per hour.

Question:
1. Should the port deploy the additional crane or not?
2. Show the step-by-step calculation of costs in both scenarios.
3. Recommend the best financial option and explain clearly why.

"""

response = client.responses.create(
    model="gpt-5-nano",
    reasoning={"effort": "medium"},
    input=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.output_text)

