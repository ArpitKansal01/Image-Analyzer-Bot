from flask import Flask, render_template, request
import os
import image_analysis as img

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', result=None)  # Pass None for the initial load

@app.route('/submit', methods=['POST'])
def submit():
    if 'user_input' not in request.files:
        return "No file part"
    
    file = request.files['user_input']
    
    if file.filename == '':
        return "No selected file"
    
    # Save the uploaded file to the uploads directory
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)
    
    # Get the prompt from the form
    prompt = request.form['prompt']
    
    # Call the main function from image_analysis and pass the image path and prompt
    response = img.main(image_path, prompt)
    
    # Render the index template with the result
    return render_template('index.html', result=response)

if __name__ == '__main__':
    app.run(debug=True)