foo = """#gw690 #fujigw690 #kodakfilm #filmphotography #shootfilm  #filmshooters #fineartfilm #exploremore #lensculture #lensculturestreets #ig_street #streetshot  #analog #6x9 #texasleica #madewithkodak #shootfilmmag  #analoguevibes  #filmphotographic #bayarea #filmwave  #dreamermagazine  #onearthmagazine #architecture #sanfrancisco #shootfilm #chicano #streetphotography #ektachrome100 #latinxartist"""


def parse_hashtag_string(hashtags: str) -> set:
    """Parses string of hashtags returns set."""
    return set([item.strip() for item in hashtags.split("#") if item != ""])


def return_hashtags(hashtag_set: set) -> str:
    """Returns a string of formatted hashtags."""
    hashtag_string = ""
    for tag in hashtag_set:
        hashtag_string += f"#{tag} "

    return hashtag_string
