# hashtag_tumbler
A python library for saving and tumbling hashtags 

`hashtag.py` contains a dictionary, hashtags. The items in hashtags are lists of hashtags, where the names define a user defined hashtag category. 


# uvloop
uvloop seems to be slightly faster, but needs to be repeatadly tested. 
- write a function to run 1000 requests 10 tens and calculate the average, save results to a dict. 
- running the requests with access_log = False seems speed things up a bit, probably because Sanic doesn't need to print to std out. 

# Todo 
- write an abstracted request funcion that can be called from 3 three different apps:
    - Sanic with async sqlite
    - Sanic with regular blocking sqlite read/write functions
    - Flask with regular sqlite functions. 