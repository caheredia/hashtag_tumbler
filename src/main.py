import subprocess

from src.hashtags import (foo, k_random_hashtags, parse_hashtag_string,
                          return_hashtags)

parsed_hashtags = parse_hashtag_string(foo)
random_parsed_set = k_random_hashtags(parsed_hashtags, 28)
data = return_hashtags(random_parsed_set)
print(data)

# copy return data to system clipboard
subprocess.run("pbcopy", universal_newlines=True, input=data)


# TODO make this a main file, capable of receiving individual groups and a number
# for example, --fuji 10 --leica 4 --landscape 4 --sanfrancsico
# and fill the remaing set with with total , defaulted to 30
# place tags in flatfiles only load them if you need a group
