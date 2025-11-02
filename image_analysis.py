from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

# Configure the API
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Initialize the model
model = "gemini-2.5-flash"

def main(image_path, prompt):
    print("Image Analysis with Gemini API")
    print("-------------------------------")

    print(f"Prompt: {prompt}")
    print(f"Response:\n")
    
    image = Image.open(image_path)
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, prompt]
)
    
    return response.text

if __name__ == "__main__":
    main('path/to/your/image.jpg', 'default prompt')  # You can remove or modify this line as needed