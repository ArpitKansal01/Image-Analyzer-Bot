import google.generativeai as genai
from PIL import Image

# Configure the API
genai.configure(api_key="AIzaSyDME1zikC3YA5ZCg2R6Q6iPMoMAJrfWk6E")  # Replace with your actual API key

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def main(image_path, prompt):
    print("Image Analysis with Gemini API")
    print("-------------------------------")

    print(f"Prompt: {prompt}")
    print(f"Response:\n")
    
    image = Image.open(image_path)
    response = model.generate_content([prompt, image])
    
    return response.text

if __name__ == "__main__":
    main('path/to/your/image.jpg', 'default prompt')  # You can remove or modify this line as needed