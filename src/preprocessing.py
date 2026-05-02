# src/preprocessing.py

import cv2
import numpy as np

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Loads an image, resizes it, and normalizes it for model input.
    """
    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    # Convert BGR (OpenCV default) to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize to target size
    img = cv2.resize(img, target_size)
    
    # Normalize to [0, 1]
    img = img.astype(np.float32) / 255.0
    
    # Add batch dimension (1, 224, 224, 3)
    img = np.expand_dims(img, axis=0)
    
    return img

def get_display_image(image_path):
    """
    Returns the original image for visualization purposes.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")
    return img
