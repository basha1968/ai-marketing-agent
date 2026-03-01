import random

topics = open("keywords.txt").read().splitlines()
products = open("affiliate_products.txt").read().splitlines()

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
