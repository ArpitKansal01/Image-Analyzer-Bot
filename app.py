from flask import Flask, render_template, request
import os
import image_analysis as img

app = Flask(__name__)

# Temporary uploads directory (optional, can use tempfile instead)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/submit', methods=['POST'])
def submit():
    if 'user_input' not in request.files:
        return "No file part"
    
    file = request.files['user_input']
    
    if file.filename == '':
        return "No selected file"
    
    # Save temporarily
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    try:
        # Get prompt text
        prompt = request.form['prompt']

        # Run image analysis
        response = img.main(image_path, prompt)

    finally:
        # Always delete the uploaded file (even if analysis fails)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    # Render the page with the result
    return render_template('index.html', result=response)

if __name__ == '__main__':
    app.run(debug=True)
