from google import genai
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()
# Get Gemini API key from environment
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"


def main(image_path, prompt):
    try:
        print("Image Analysis with Gemini API")
        print("-------------------------------")
        print(f"Prompt: {prompt}")

        # Open image
        image = Image.open(image_path)

        # Send image + prompt to Gemini
        response = client.models.generate_content(
            model=MODEL,
            contents=[
                image,
                prompt
            ]
        )

        return response.text

    except Exception as e:
        print(f"Gemini analysis error: {e}")
        raise