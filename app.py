import uuid
from flask import Flask, render_template, request, redirect, url_for
import files

app = Flask(__name__)

posts = []
posts = files.load_posts()


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_post = {
            "id": str(uuid.uuid4()),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content"),
        }
        posts.append(new_post)
        print(posts)
        files.save_posts(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run()
