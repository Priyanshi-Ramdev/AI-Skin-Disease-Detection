# src/model.py

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

def build_model(num_classes=7):
    """
    Builds a transfer learning model using MobileNetV2.
    HAM10000 has 7 classes.
    """
    # Load base model with pre-trained ImageNet weights
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    # Freeze the base model
    base_model.trainable = False
    
    # Add custom head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(256, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    
    return model

# Class mapping for HAM10000
CLASS_NAMES = {
    0: "akiec",  # Actinic keratoses
    1: "bcc",    # Basal cell carcinoma
    2: "bkl",    # Benign keratosis-like lesions
    3: "df",     # Dermatofibroma
    4: "mel",    # Melanoma
    5: "nv",     # Melanocytic nevi
    6: "vasc"    # Vascular lesions
}
