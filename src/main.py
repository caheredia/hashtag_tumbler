import subprocess

from src.hashtag_data import chicano, film, fuji, leica, sanfrancisco, street
from src.hashtags import k_random_hashtags, parse_hashtag_string, return_hashtags

hashtags = chicano + film
random_list = k_random_hashtags(hashtags, 5)
data = return_hashtags(random_list)

# copy return data to system clipboard
subprocess.run("pbcopy", universal_newlines=True, input=data)


# TODO make this a main file, capable of receiving individual groups and a number
# for example, --fuji 10 --leica 4 --landscape 4 --sanfrancsico
# and fill the remaing set with with total , defaulted to 30
# place tags in flatfiles only load them if you need a group
