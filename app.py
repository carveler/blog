from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with open("posts.json", "r") as posts_obj:
        blog_posts = json.load(posts_obj)    
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run()
