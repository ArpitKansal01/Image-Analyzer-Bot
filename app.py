from flask import Flask, render_template, request
import os
import uuid
import image_analysis as img
import markdown

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB


@app.route("/")
def index():
    return render_template("index.html", result=None)


@app.route("/submit", methods=["POST"])
def submit():
    if "user_input" not in request.files:
        return render_template(
            "index.html",
            result="No image file was uploaded."
        )

    file = request.files["user_input"]

    if not file or file.filename == "":
        return render_template(
            "index.html",
            result="No image was selected."
        )

    prompt = request.form.get("prompt", "").strip()

    if not prompt:
        return render_template(
            "index.html",
            result="Please enter a prompt."
        )

    # Generate a unique temporary filename
    extension = os.path.splitext(file.filename)[1].lower()
    image_path = os.path.join(
        UPLOAD_FOLDER,
        f"{uuid.uuid4()}{extension}"
    )

    try:
        file.save(image_path)

        # Run image analysis
        response = img.main(image_path, prompt)
        response = markdown.markdown(response)
        return render_template(
            "index.html",
            result=response
        )

    except Exception as e:
        app.logger.exception("Image analysis failed")

        return render_template(
            "index.html",
            result=f"Error analyzing image: {str(e)}"
        ), 500

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)