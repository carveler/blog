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


@app.route("/delete/<post_id>")
def delete(post_id):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            files.save_posts(posts)
            return redirect(url_for("index"))
    return "Post not found"


def fetch_post_by_id(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["author"] = request.form["author"]
        post['content'] = request.form['content']
        files.save_posts(posts)
        return redirect(url_for("index"))
    return render_template("update.html", post=post)


if __name__ == "__main__":
    app.run()
