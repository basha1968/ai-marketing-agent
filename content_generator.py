import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

topic = "Workplace Safety Tips"

response = openai.ChatCompletion.create(
model="gpt-4o-mini",
messages=[
{"role": "user", "content": f"Write a blog article about {topic} with SEO headings."}
]
)

article = response.choices[0].message.content

print(article)

with open("article.txt", "w") as f:
    f.write(article)
