from openai import OpenAI
import json
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
client = OpenAI()

class ContainerBooking(BaseModel):
    origin_port: str
    destination_port: str
    departure_date: str
    container_size: str

response = client.responses.parse(      # Remeber, we are parsing, not creating a response
    model="gpt-5-nano",
    input= [
        {"role": "system", "content": "Extract the container booking information."},
        {"role": "user", "content": "I need to book a 40ft container from Mumbai to Rotterdam, departure on 25th October."},
    ],
    text_format= ContainerBooking,

)

#print("=== PARSED RESPONSE ===")
#print(response)


print(response.output_parsed)
