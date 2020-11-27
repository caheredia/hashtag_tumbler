from random import randint

foo = """#gw690 #fujigw690 #kodakfilm #filmphotography #shootfilm  #filmshooter #fineartfilm #exploremore #lensculture #lensculturestreets #ig_street #streetshot  #analog #6x9 #texasleica #madewithkodak #shootfilmmag  #analoguevibes  #filmphotographic #bayarea #filmwave  #dreamermagazine  #onearthmagazine #architecture #sanfrancisco #shootfilm #chicano #streetphotography #ektachrome100 #latinxartist"""


def parse_hashtag_string(hashtags: str) -> set:
    """Parses string of hashtags returns set."""
    return set([item.strip() for item in hashtags.split("#") if item != ""])


def k_random_hashtags(hashtag_set: set, k: int) -> set:
    """Returns a k size set of elements."""
    hashtag_list = list(hashtag_set)
    random_elements = [
        hashtag_list.pop(randint(0, len(hashtag_list) - 1)) for _ in range(k)
    ]
    return set(random_elements)


def return_hashtags(hashtag_set: set) -> str:
    """Returns a string of formatted hashtags."""
    hashtag_string = [f"#{tag} " for tag in hashtag_set]

    return "".join(hashtag_string)


# sudo main routine
parsed_hashtags = parse_hashtag_string(foo)
random_parsed_set = k_random_hashtags(parsed_hashtags, 28)
print(return_hashtags(random_parsed_set))
