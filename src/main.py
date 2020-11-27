from src.hashtags import (foo, k_random_hashtags, parse_hashtag_string,
                          return_hashtags)

parsed_hashtags = parse_hashtag_string(foo)
random_parsed_set = k_random_hashtags(parsed_hashtags, 28)
print(return_hashtags(random_parsed_set))

# TODO make this a main file, capable of receiving individual groups and a number 
# for example, --fuji 10 --leica 4 --landscape 4 --sanfrancsico
# and fill the remaing set with with total , defaulted to 30
