# app.py
from flask import Flask, request, jsonify
from simple_random_model import RandomModel
import os
from datetime import datetime

# Initialize the Flask app and model
app = Flask(__name__)
model = RandomModel()

# Define directory to save uploaded images
UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image is uploaded
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Retrieve the image from the request
    image = request.files['image']

    # Save the image to the upload directory with a timestamped name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(UPLOAD_FOLDER, f"{timestamp}_{image.filename}")
    image.save(image_path)

    # Generate prediction using the RandomModel
    prediction, confidence = model.predict(image_path)

    # Return the prediction and confidence as a JSON response
    return jsonify({
        "prediction": prediction,
        "confidence": f"{confidence}%"
    })

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)
