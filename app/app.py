from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Get the absolute path to the directory where this file (app.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))

# Ensure uploads folder is inside app/static/uploads
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model (adjust this path if needed)
model = load_model(os.path.join(BASE_DIR, '..', 'model', 'model.h5'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400

        # Save file inside app/static/uploads
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Preprocess and predict
        img = image.load_img(filepath, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        prediction = model.predict(img_array)

        label = 'Dog' if prediction[0][0] > 0.5 else 'Cat'

        # Image path for HTML rendering (relative to /static/)
        return render_template('index.html', prediction=label, image_path='uploads/' + file.filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
