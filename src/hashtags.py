from random import randint


def parse_hashtag_string(hashtags: str) -> list:
    """Parses string of hashtags returns list."""
    return list(set([item.strip() for item in hashtags.split("#") if item != ""]))


def k_random_hashtags(hashtag_list: list, k: int) -> set:
    """Returns a k size list of elements."""
    random_elements = [
        hashtag_list.pop(randint(0, len(hashtag_list) - 1)) for _ in range(k)
    ]
    return random_elements


def return_hashtags(hashtag_list: list) -> str:
    """Returns a string of formatted hashtags from a list."""
    hashtag_string = [f"#{tag} " for tag in hashtag_list]

    print("\n".join(hashtag_string))
    return "\n".join(hashtag_string)
