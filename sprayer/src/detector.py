import base64
from openai import OpenAI
from dotenv import load_dotenv
import os



load_dotenv()

open_api_key = os.getenv("OPEN_API_KEY")




class Detector:
    def __init__(self):
        self.client = OpenAI(api_key = open_api_key)
        self.MAX_RETRIES = 10
        self.plant_types = ['Cactus', 'Grass', 'Succulent', 'Parsley', 'Bottle']


    def detect_plant(self, image):
        for i in range(self.MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Output the plant type or Bottle and only the plant type in one word 'Cactus', 'Grass', 'Succulent', 'Parsley', or 'Bottle' if the image's object of interest contains the plant or Bottle",
                        },
                        {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{image}"
                        },
                        },
                    ],
                    }
                ],
                )
                
                res = response.choices[0].message.content
                print('gpt response: ' + res)

                if res in self.plant_types:
                    return True, res
                else:
                    return False, None
                break
            except Exception as e:
                print('failed times: ', i, 'error: ', e)


    def is_plant(self, image): # expect base64 utf 8 string
        for i in range(self.MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Output in one word true or false if the image contains any plant",
                        },
                        {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{image}"
                        },
                        },
                    ],
                    }
                ],
                )
                res = response.choices[0].message.content

                if res in ["True", 'true']:
                    return True
                else:
                    return False
                break
            except Exception as e:
                print('failed times: ', i, 'error: ', e)



