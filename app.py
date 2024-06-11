import uuid
from flask import Flask, render_template, request, redirect, url_for
import files

app = Flask(__name__)

posts = files.load_posts()


@app.route("/")
def index():
    """
    Route for the main index page.
    Return:
         the rendered 'index.html' template with the list of posts.
    """
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Route to add a new post.
    If the method is POST, a new post is created and saved.
    Redirects to the index page upon successful addition.
    """
    if request.method == "POST":
        new_post = {
            "id": str(uuid.uuid4()),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content"),
            "likes": 0,
        }
        posts.append(new_post)
        print(posts)
        files.save_posts(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<post_id>")
def delete(post_id):
    """
    Route to delete a post by its ID.
    If the post is found, it is removed and the posts are saved.
    Redirects to the index page upon successful deletion.
    """
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            files.save_posts(posts)
            return redirect(url_for("index"))
    return "Post not found"


def fetch_post_by_id(post_id):
    """
    Helper function to fetch a post by its ID.
    Returns the post if found, otherwise returns None.
    """
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    """
    Route to update an existing post by its ID.
    If the method is POST, the post is updated and saved.
    Returns the 'update.html' template for GET requests.
    """
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["author"] = request.form["author"]
        post["content"] = request.form["content"]
        files.save_posts(posts)
        return redirect(url_for("index"))
    return render_template("update.html", post=post)


@app.route("/likes/<post_id>", methods=["GET", "POST"])
def likes(post_id):
    """
    Route to increment the 'likes' count of a post by its ID.
    If the method is POST and the post is found, its 'likes' are incremented.
    Redirects to the index page upon successful increment.
    """
    if request.method == "POST":
        post = fetch_post_by_id(post_id)
        if post is None:
            return "Post not found", 404
        post["likes"] += 1
        files.save_posts(posts)
        return redirect(url_for("index"))
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run()
