import os

products = []

with open("affiliate_products.txt") as f:
    products = f.readlines()

content = "AI Generated Marketing Article\n\n"

for product in products:
    name, link = product.strip().split("|")
    content += f"Check out {name}: {link}\n"

os.makedirs("output", exist_ok=True)

with open("output/blog_post.txt", "w") as f:
    f.write(content)

print("Content generated successfully")
