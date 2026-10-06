from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Try to load the model with custom objects if needed
custom_objects = {}  # Add any custom layers or functions in this dictionary

try:
    model = tf.keras.models.load_model('x_model.h5', custom_objects=custom_objects)
    print("Model loaded successfully!")
except ValueError as e:
    print(f"Error loading model: {e}")
    model = None

# Ensure the model is compiled
if model:
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Define the classes
class_names = ['class_0', 'class_1']  # Replace with your class names

# Create folder to store uploaded images
UPLOAD_FOLDER = 'static/uploaded_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded image
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(img_path)

        # Load the image and process it
        img = image.load_img(img_path, target_size=(224, 224))  # Resize as per model input
        img_array = image.img_to_array(img) / 255.0  # Normalize image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make predictions if the model is loaded correctly
        if model:
            prediction = model.predict(img_array)
            predicted_class = 1 if prediction[0] > 0.5 else 0  # Apply threshold for binary classification
            predicted_class_name = class_names[predicted_class]
            return render_template('index.html', filename=file.filename, prediction=predicted_class_name)
        else:
            return render_template('index.html', filename=file.filename, prediction="Model error")

if __name__ == '__main__':
    app.run(debug=True)
