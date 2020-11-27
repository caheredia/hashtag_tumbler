from src.hashtags import (foo, k_random_hashtags, parse_hashtag_string,
                          return_hashtags)

parsed_hashtags = parse_hashtag_string(foo)
random_parsed_set = k_random_hashtags(parsed_hashtags, 28)
print(return_hashtags(random_parsed_set))
