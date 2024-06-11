import json

FILE_PATH = "posts.json"


def load_posts():
    """
        Load posts from a JSON file.
        Returns:
            a list of posts or None if the file is missing.
    """
    try:
        with open(FILE_PATH, "r") as posts_obj:
            posts = json.load(posts_obj)
            return posts
    except FileNotFoundError:
        print("Error: The storage file was not found.")


def save_posts(posts):
    """
    Save posts to a JSON file

    Args:
        posts (list): list of posts dictionaries.
    """
    try:
        with open(FILE_PATH, "w") as posts_obj:
            json.dump(posts, posts_obj, indent=4)
    except FileNotFoundError:
        print("Error: The storage file was not found.")
