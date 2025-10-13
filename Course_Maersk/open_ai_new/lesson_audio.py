from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
OpenAI.api_key  = os.getenv('OPENAI_API_KEY')

response = client.responses.create(
    model="gpt-5-nano",
    input="Generate audio saying: Your container MAEU1234567 has arrived at Mumbai Port and is ready for pickup.",
    tools=[{"type": "audio_generation"}]
)

# Save the audio to a file
audio_data = [
    output.result
    for output in response.output
    if output.type == "audio_generation_call"
]

if audio_data:
    with open("shipment_notification.mp3", "wb") as f:
        f.write(audio_data[0])
