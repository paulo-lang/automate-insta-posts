import base64
from openai import OpenAI

def getChatGPTImage(prompt:str):
    client = OpenAI() 

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        tools=[{"type": "image_generation"}],
    )

    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    if image_data:
        image_base64 = image_data[0]
        with open("otter.png", "wb") as f:
            f.write(base64.b64decode(image_base64))
