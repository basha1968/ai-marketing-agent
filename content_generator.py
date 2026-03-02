import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "affiliate_products.txt")

products = open(file_path).read().splitlines()
topic = random.choice(topics)
product = random.choice(products)

name,link = product.split("|")

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
