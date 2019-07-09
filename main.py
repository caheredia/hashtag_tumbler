from random import sample
from json import dumps, load

HASHTAG_FILE = "hashtags.py"


def load_hashtags():
    with open(HASHTAG_FILE, "r") as file:
        hashtags = load(file)
    return hashtags


hashtags = load_hashtags()


def random_hashtags(category, n_samples=5):
    """Return an n_samples from category."""
    random_samples = sample(hashtags[category], n_samples)
    return random_samples


def print_tags(tags):
    """Prints a list of hashtags with hashtag prefix."""
    for tag in tags:
        print(f"#{tag}")


def add_category(category):
    hashtags[category] = []


def add_hashtags(category, new_hashtags):

    if category not in hashtags.keys():
        add_category(category)
    for tag in new_hashtags:
        if tag not in hashtags[category]:
            hashtags[category].append(tag)


def save_hashtags():
    with open(HASHTAG_FILE, "w") as file:
        file.write(dumps(hashtags))


def main():

    add_category("leica_camera")
    add_hashtags("leica_camera", ["leicamp"])
    add_hashtags("san_francisco", ["bayarea"])
    save_hashtags()
    print(hashtags)


if __name__ == "__main__":
    main()
