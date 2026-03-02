import os
import random

# Get repo directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load affiliate products
products_file = os.path.join(base_dir, "affiliate_products.txt")

with open(products_file, "r") as f:
    products = f.read().splitlines()

# Example topics (or load from keywords.txt)
topics = [
    "Warehouse Safety Best Practices",
    "How to Reduce Warehouse Accidents",
    "Essential PPE for Warehouse Workers",
    "Forklift Safety Tips for Beginners"
]

topic = random.choice(topics)
product = random.choice(products)

name, link = product.split("|")

article = f"""
TITLE: {topic}

INTRODUCTION
Warehouse safety and material control are critical for efficient operations.

RECOMMENDED PRODUCT
{name}

Buy here:
{link}

CONCLUSION
Proper safety procedures reduce accidents and improve productivity.
"""

print(article)
