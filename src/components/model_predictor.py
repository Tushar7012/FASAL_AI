import tensorflow as tf
from PIL import Image
import numpy as np
import os
from src.utils.common import read_yaml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_FILE_PATH = os.path.join(PROJECT_ROOT, 'src', 'config', 'config.yaml')
config = read_yaml(CONFIG_FILE_PATH)

MODEL_PATH = "C:/Users/td334/Downloads/plant_disease_model_v1.h5"

IMAGE_SIZE = (config['model']['image_size'], config['model']['image_size'])
CLASS_NAMES = config['class_names']

model = tf.keras.models.load_model(MODEL_PATH)

def predict_disease(image_data):
    """
    Takes image data, preprocesses it, and predicts the disease using the loaded model.
    """
    image = Image.open(image_data).resize(IMAGE_SIZE)
    image_array = np.array(image)
    image_batch = np.expand_dims(image_array, 0)

    predictions = model.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    return predicted_class, confidence
