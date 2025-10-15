# Lot of time Model alone can not solve the Problems
# We need to give it some tools to help it solve the problems
# for example : Web search tool to get latest information from the web
# Calculator tool to do mathematical calculations
# Calendar tool to manage your schedule

# In Order to make use Custom Function calling we need to define the tools Schema
# This is done using JSON Schema
# Then we need to embed the tool schema in the prompt and define the function calling behaviour
# This is done by setting the function_call parameter to "auto" or "none" or
# We can also use the inbuilt tools provided by OpenAI

# Lesson1 Custom Tools and Function Calling
# First Define The Tool Schema (JSON Schema as suggested by OpenAI)
# https://platform.openai.com/docs/guides/function-calling (Link for explanation of JSON Schema)
from openai import OpenAI
import json
import os
from dotenv import load_dotenv


load_dotenv()

# Use environment variable for API key (secure approach)
# Create a .env file with: OPENAI_API_KEY=your_actual_api_key_here

client = OpenAI()  # Will automatically use OPENAI_API_KEY from environment



# 1. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "get_shipment_status",
        "description": "Get the current status and location of a shipment by container number.",
        "parameters": {
            "type": "object",
            "properties": {
                "container_number": {
                    "type": "string",
                    "description": "The container tracking number (e.g., MAEU1234567)",
                },
            },
            "required": ["container_number"],
        },
    },
]

def get_shipment_status(container_number):
    return f"{container_number}: Your container is currently at Mumbai Port, scheduled to depart on 15th October."

# Create a running input list we will add to over time
input_list = [
    {"role": "user", "content": "Where is my shipment? Container number is MAEU1234567."}
]

# 2. Prompt the model with tools defined
resp1 = client.responses.create(
    model="gpt-5-nano",
    tools=tools,
    input=input_list,
    instructions="Use Tools if you find it necessary."

)

#print("=== RAW RESPONSE ===")
#print(response.output)




# 5️⃣ Append model's structured tool call
for item in resp1.output:
    if item.type == "function_call":
        input_list.append({
            "type": "function_call",
            "call_id": item.call_id,
            "name": item.name,
            "arguments": item.arguments
        })

# 6️⃣ Execute the tool and append its output
for item in resp1.output:
    if item.type == "function_call" and item.name == "get_shipment_status":
        args = json.loads(item.arguments)                 # Parse JSON → dict
        container_number = args["container_number"]       # Extract argument
        result = get_shipment_status(container_number)    # Run Python function

        input_list.append({
            "type": "function_call_output",
            "call_id": item.call_id,                      # Must match call_id
            "output": result                              # Plain string is fine
        })

# ✅ 7️⃣ Second call — model gives final answer
resp2 = client.responses.create(
    model="gpt-5",
    instructions="Respond only with the shipment status returned by the tool. Do not add or modify anything.",
    tool_choice="none",      # ensures no further tool calling
    input=input_list,
)




# 5. The model should be able to give a response!
print("Final output:")
print(resp2.model_dump_json(indent=2))
print("\n" + resp2.output_text)
