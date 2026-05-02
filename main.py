# main.py

import argparse
import os
import numpy as np
import cv2
from src.model import build_model, CLASS_NAMES
from src.preprocessing import preprocess_image, get_display_image
from src.recommendation import get_recommendations

def main():
    parser = argparse.ArgumentParser(description="AI Skin Disease Detection System")
    parser.add_argument("--image", type=str, required=True, help="Path to the skin image")
    parser.add_argument("--skin_type", type=str, default="oily", choices=["oily", "dry", "sensitive", "combination"], help="User skin type")
    parser.add_argument("--model_path", type=str, default="models/skin_disease_model.h5", help="Path to saved model weights")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.image):
        print(f"Error: Image path '{args.image}' not found.")
        return

    print(f"--- Processing Image: {args.image} ---")
    
    # 1. Build Model
    model = build_model()
    
    # 2. Load Weights (if they exist)
    if os.path.exists(args.model_path):
        print(f"Loading weights from {args.model_path}...")
        model.load_weights(args.model_path)
    else:
        print("Warning: Model weights not found. Using randomly initialized weights for demonstration.")

    # 3. Preprocess Image
    try:
        processed_img = preprocess_image(args.image)
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return

    # 4. Inference
    predictions = model.predict(processed_img, verbose=0)
    class_idx = np.argmax(predictions[0])
    confidence = predictions[0][class_idx]
    disease_code = CLASS_NAMES[class_idx]

    # 5. Get Recommendations
    rec = get_recommendations(disease_code, args.skin_type)

    # 6. Display Results
    print("\n" + "="*50)
    print(f"RESULTS FOR: {args.image}")
    print(f"Detected Condition: {disease_code.upper()} ({rec['description']})")
    print(f"Confidence Score: {confidence:.2%}")
    print(f"Skin Type Input: {args.skin_type.capitalize()}")
    print("="*50)
    
    print("\nMEDICATED RECOMMENDATIONS:")
    for item in rec['medicated_products']:
        print(f" - {item}")
        
    print("\nHERBAL RECOMMENDATIONS:")
    for item in rec['herbal_products']:
        print(f" - {item}")

    print("\nLIFESTYLE ADVICE:")
    print(f" - {rec['lifestyle_advice']}")

    print("\nSKIN TYPE SPECIFIC ADVICE:")
    print(f" - {rec['skin_type_specific_advice']}")
    print("="*50)

    # 7. Visualization (Optional - Show image with label)
    # Note: In a headless environment, this won't show a window, so we'll save it.
    output_img = get_display_image(args.image)
    cv2.putText(output_img, f"{disease_code}: {confidence:.2%}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    output_path = "data/processed/last_prediction.jpg"
    cv2.imwrite(output_path, output_img)
    print(f"\nVisualization saved to: {output_path}")

if __name__ == "__main__":
    main()
