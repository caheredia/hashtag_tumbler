from random import sample

from src.database.hashtags import data


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
        file.write(f"tag_dict={hashtags}")


def remove_category(category):
    hashtags.pop(category, None)


def remove_hashtags(category, del_hashtags):
    for hashtag in del_hashtags:
        if hashtag in hashtags[category]:
            hashtags[category].remove(hashtag)


def build_long_list(categories):
    tags = []
    for category in set(categories):
        tags += random_hashtags(category)
    return tags


def extract_hashtags_from_file(filename):
    with open(filename) as file:
        copied_string = file.read()
        for item in copied_string.split("#"):
            print(item.strip())


def main():
    for theme in data:
        print(theme)
        for group in data[theme]:
            print( "\t",group)
            for hashtag in data[theme][group]:
                print("\t\t", hashtag)

if __name__ == "__main__":
    main()

"""    add_hashtags(
        "bw",
        [
            "bw_photooftheday",
            "blackandwhitephotography",
            "bnwphotostories",
            "bnw_life",
            "blackandwhitephotography",
            "35mmfilm",
            "blackandwhite",
            "bwphoto",
        ],
    )
    save_hashtags()"""
