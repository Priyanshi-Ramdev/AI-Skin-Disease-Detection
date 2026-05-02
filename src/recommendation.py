# src/recommendation.py

RECOMMENDATIONS = {
    "akiec": {  # Actinic keratoses
        "description": "Precancerous skin patches caused by sun damage.",
        "medicated": ["Fluorouracil cream", "Imiquimod cream", "Solaraze gel"],
        "herbal": ["Green tea extract serum", "Aloe vera gel", "Flaxseed oil"],
        "lifestyle": "Avoid peak sun hours and use high SPF sunscreen."
    },
    "bcc": {  # Basal cell carcinoma
        "description": "A type of skin cancer that begins in the basal cells.",
        "medicated": ["Imiquimod", "Vismodegib (for advanced cases)", "Consult Surgeon"],
        "herbal": ["Milk thistle extract (topical)", "Aloe vera", "Chamomile"],
        "lifestyle": "Immediate dermatologist consultation required."
    },
    "bkl": {  # Benign keratosis-like lesions
        "description": "Non-cancerous skin growths like seborrheic keratoses.",
        "medicated": ["Tretinoin cream", "Glycolic acid peels", "Cryotherapy"],
        "herbal": ["Witch hazel", "Apple cider vinegar (diluted)", "Tea tree oil"],
        "lifestyle": "Usually harmless but can be removed for cosmetic reasons."
    },
    "df": {  # Dermatofibroma
        "description": "Common benign fibrous nodules.",
        "medicated": ["Corticosteroid injections", "Liquid nitrogen"],
        "herbal": ["Vitamin E oil", "Lavender oil", "Coconut oil"],
        "lifestyle": "Monitor for changes in size or color."
    },
    "mel": {  # Melanoma
        "description": "The most serious type of skin cancer.",
        "medicated": ["Surgical excision", "Immunotherapy", "Targeted therapy"],
        "herbal": ["Turmeric (as supplement, not treatment)", "Ginger extract"],
        "lifestyle": "URGENT medical attention needed."
    },
    "nv": {  # Melanocytic nevi (Moles)
        "description": "Common moles; usually benign.",
        "medicated": ["None needed", "Surgical removal if suspicious"],
        "herbal": ["Castor oil (for skin softening)", "Honey"],
        "lifestyle": "Monitor using the ABCDE rule (Asymmetry, Border, Color, Diameter, Evolving)."
    },
    "vasc": {  # Vascular lesions
        "description": "Skin conditions affecting blood vessels (e.g., angiomas).",
        "medicated": ["Laser therapy", "Sclerotherapy", "Propranolol"],
        "herbal": ["Witch hazel", "Horse chestnut extract", "Arnica gel"],
        "lifestyle": "Avoid excessive heat or skin trauma."
    }
}

SKIN_TYPE_ADVICE = {
    "oily": "Choose oil-free, non-comedogenic formulations. Look for Salicylic acid or Niacinamide.",
    "dry": "Use rich, hydrating creams with Ceramides or Hyaluronic acid. Avoid alcohol-based toners.",
    "sensitive": "Opt for fragrance-free, hypoallergenic products. Patch test all new treatments.",
    "combination": "Use lightweight moisturizers on the T-zone and richer creams on cheeks."
}

def get_recommendations(disease_code, skin_type):
    """
    Returns recommendations based on disease and skin type.
    """
    disease_info = RECOMMENDATIONS.get(disease_code, {
        "description": "Unknown condition.",
        "medicated": ["Consult a dermatologist"],
        "herbal": ["N/A"],
        "lifestyle": "Seek professional advice."
    })
    
    skin_advice = SKIN_TYPE_ADVICE.get(skin_type.lower(), "Consult a specialist for skin type specific advice.")
    
    return {
        "disease": disease_code,
        "description": disease_info["description"],
        "medicated_products": disease_info["medicated"],
        "herbal_products": disease_info["herbal"],
        "lifestyle_advice": disease_info["lifestyle"],
        "skin_type_specific_advice": skin_advice
    }
