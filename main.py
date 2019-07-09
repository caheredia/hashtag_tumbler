from hashtag import hashtags
from random import sample


def random_hashtags(category, n_samples=5):
    """Return an n_samples from category."""
    random_samples = sample(hashtags[category], n_samples)
    return random_samples


def print_tags(tags):
    """Prints a list of hashtags with hashtag prefix."""
    for tag in tags:
        print(f"#{tag}")


def main():
    print_tags(random_hashtags("instagram"))


if __name__ == "__main__":
    main()
