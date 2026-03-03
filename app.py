from flask import Flask
import subprocess
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your GitHub Pages dashboard to connect

@app.route("/run-content-generator")
def run_content_generator():
    try:
        # Run the content generator script (same directory level)
        result = subprocess.run(
            ["python", "content_generator.py"],
            check=True,
            capture_output=True,
            text=True
        )
        # If the script produced errors/warnings, log them
        if result.stderr:
            print("Script stderr:", result.stderr)  # visible in Render logs

        # Read the generated output file (same folder level)
        with open("output/blog_post.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return content

    except subprocess.CalledProcessError as e:
        error_msg = f"Script failed with exit code {e.returncode}\nStderr: {e.stderr}"
        return error_msg, 500
    except FileNotFoundError as e:
        return f"File not found: {str(e)}", 500
    except Exception as e:
        return f"Unexpected error in content generator: {str(e)}", 500


@app.route("/run-social-media")
def run_social_media():
    try:
        # Run LinkedIn script
        linkedin_result = subprocess.run(
            ["python", "linkedin_post.py"],
            check=True,
            capture_output=True,
            text=True
        )
        if linkedin_result.stderr:
            print("LinkedIn stderr:", linkedin_result.stderr)

        # Run Blogger script
        blogger_result = subprocess.run(
            ["python", "publish_blogger.py"],
            check=True,
            capture_output=True,
            text=True
        )
        if blogger_result.stderr:
            print("Blogger stderr:", blogger_result.stderr)

        return "Social media scripts ran successfully! (LinkedIn + Blogger)"

    except subprocess.CalledProcessError as e:
        error_msg = f"Script failed with exit code {e.returncode}\nStderr: {e.stderr}"
        return error_msg, 500
    except Exception as e:
        return f"Unexpected error in social media scripts: {str(e)}", 500


# Health check route — open this URL to confirm backend is alive
@app.route("/")
def home():
    return "Backend is running! Test endpoints: /run-content-generator or /run-social-media"


if __name__ == "__main__":
    # Render.com assigns a dynamic port via environment variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
