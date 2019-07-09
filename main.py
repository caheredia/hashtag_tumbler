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
    if category not in hashtags.keys():
        hashtags[category] = []


def add_hashtags(category, new_hashtags):
    try:
        for tag in new_hashtags:
            if tag not in hashtags[category]:
                hashtags[category].append(tag)
    except KeyError:
        add_category(category)
        add_hashtags(category, new_hashtags)


def save_hashtags():
    with open(HASHTAG_FILE, "w") as file:
        file.write(dumps(hashtags))


def remove_category(category):
    hashtags.pop(category, None)


def remove_hashtags(category, del_hashtags):
    for hashtag in del_hashtags:
        if hashtag in hashtags[category]:
            hashtags[category].remove(hashtag)


def main():
    print_tags(random_hashtags("leica_camera"))


if __name__ == "__main__":
    main()