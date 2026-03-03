from flask import Flask, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Important: allows your GitHub Pages dashboard to connect

@app.route("/run-content-generator")
def run_content_generator():
    try:
        # Run your content script (path goes up one level to root)
        subprocess.run(["python", "../content_generator.py"], check=True, capture_output=True)
        # Read the generated output file
        with open("../output/blog_post.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error in content generator: {str(e)}", 500

@app.route("/run-social-media")
def run_social_media():
    try:
        # Run your social scripts
        subprocess.run(["python", "../linkedin_post.py"], check=True, capture_output=True)
        subprocess.run(["python", "../publish_blogger.py"], check=True, capture_output=True)
        return "Social media scripts ran successfully! (LinkedIn + Blogger)"
    except Exception as e:
        return f"Error in social scripts: {str(e)}", 500

# Optional: simple health check route to confirm backend is alive
@app.route("/")
def home():
    return "Backend is running! Use /run-content-generator or /run-social-media"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
