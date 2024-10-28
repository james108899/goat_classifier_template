from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to enable cross-origin requests
from simple_random_model import RandomModel
import os
from datetime import datetime

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)  # This allows all origins to access the endpoints

model = RandomModel()

# Define the /predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image is uploaded
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Retrieve the image from the request
    image = request.files['image']

    # Save the image to the upload directory with a timestamped name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    upload_folder = "uploaded_images"
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, f"{timestamp}_{image.filename}")
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
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
