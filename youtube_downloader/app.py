from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Create downloads folder if not exists
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        file_path = os.path.join(DOWNLOAD_FOLDER, yt.title + ".mp4")
        video.download(DOWNLOAD_FOLDER)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

# Run on Render with host 0.0.0.0
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
