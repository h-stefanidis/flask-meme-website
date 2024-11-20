import requests
import logging
import random
from flask import Flask, render_template

app = Flask(__name__)

import random

def get_meme():
    url = "https://api.imgflip.com/get_memes"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "data" in data and "memes" in data["data"] and len(data["data"]["memes"]) > 0:
            memes = data["data"]["memes"]
            meme = random.choice(memes)  # Select a random meme
            return meme["url"], "Imgflip"
        else:
            logging.warning("Unexpected API response structure.")
            return None, None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching meme: {e}")
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host='0.0.0.0')