import json

FILE_PATH = "posts.json"


def load_posts():
    """
    Loads movie data from the JSON file and returns it as a list of
    dictionaries.

    Returns:
        list: List of movie dictionaries.
    """
    try:
        with open(FILE_PATH, "r") as posts_obj:
            posts = json.load(posts_obj)
            return posts
    except FileNotFoundError:
        print("Error: The storage file was not found.")


def save_posts(posts):
    """
    Saves the movie data to the JSON file.

    Args:
        posts (list): List of movie dictionaries.
    """
    try:
        with open(FILE_PATH, "w") as posts_obj:
            json.dump(posts, posts_obj, indent=4)
    except FileNotFoundError:
        print("Error: The storage file was not found.")
