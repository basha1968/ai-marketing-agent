import os
import random

# Load affiliate products
products = []
with open("affiliate_products.txt", "r", encoding="utf-8") as f:
    products = [line.strip() for line in f if line.strip()]

# Basic article structure
article_title = "Top Recommended Products for Your Needs"
introduction = (
    "In today's world, finding the right products can save you time, money, and effort. "
    "We've handpicked some of the best products available online to make your life easier.\n\n"
)

# Generate dynamic product sections
product_sections = ""
for product in products:
    name, link = product.split("|")
    benefits = [
        f"{name} offers incredible value for its price.",
        f"Many users have praised {name} for its reliability and performance.",
        f"If you're looking for quality and affordability, {name} is a great choice."
    ]
    product_sections += (
        f"### {name}\n"
        f"{random.choice(benefits)}\n"
        f"Buy here: [Link]({link})\n\n"
    )

# Conclusion
conclusion = (
    "Choosing the right product doesn't have to be hard. "
    "We hope this list helps you make informed decisions and find exactly what you need.\n"
)

# Combine all parts
article_content = f"# {article_title}\n\n{introduction}{product_sections}{conclusion}"

# Save output
os.makedirs("output", exist_ok=True)
output_file = "output/blog_post.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(article_content)

print(f"Content generated successfully! Saved to {output_file}")
