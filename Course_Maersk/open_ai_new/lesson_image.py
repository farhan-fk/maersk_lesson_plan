
from openai import OpenAI
import os
import base64
from dotenv import load_dotenv
load_dotenv()



client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Generate an image of a large blue Maersk container ship docked at Mumbai Port during sunset",
    tools=[{"type": "image_generation"}],
)

print(response)
# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("maersk_ship.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
