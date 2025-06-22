# wardrobe_utils.py
from PIL import Image
import random

# Simulated color detection
CLOTHING_CATEGORIES = ["Top", "Bottom", "Footwear", "Outerwear"]
COLOR_LABELS = ["red", "blue", "black", "white", "green", "yellow"]


def analyze_clothing(image: Image.Image):
    # Simulated label extractor
    label = random.choice(CLOTHING_CATEGORIES)
    color = random.choice(COLOR_LABELS)
    return label, color


def suggest_outfits(wardrobe_items):
    # Match random top + bottom + footwear if available
    outfit = {}
    for item in wardrobe_items:
        label, color = item["label"], item["color"]
        if label not in outfit:
            outfit[label] = color

    return outfit
