from sanic import Blueprint
from sanic.response import json

database_v1 = Blueprint('database_v1', url_prefix='/database', version="v1")
database_v1.__doc__ = "database REST API"


# turn this whole function into an async function that calls by "/themes/all"
async def get_all_values(db):
    cursor = await db.execute('SELECT DISTINCT themes FROM hashtags')
    rows = await cursor.fetchall()
    await cursor.close()

    rows = [item[0] for item in rows]
    return rows


@database_v1.route("/stamp", methods=["POST"])
async def post(request, db):
    stamp = request.json["stamp"]
    await db.execute("INSERT INTO timestamps VALUES (:stamp)", {"stamp": stamp})
    await db.commit()
    return json({"saved": stamp}, status=201)


@database_v1.route("/themes/<method>", methods=["GET"])
async def themes(request, method, db):
    """Returns a list of themes.

    Parameters
    ----------
    method : str
        method to query layer
    db : aiosqlite object
        database connection

    Returns
    -------
    list
        List of values
    """
    # get all themes
    methods = {'all': get_all_values}

    return json({'data': themes})


def get_all(theme=None, group=None, hashtag=None):
    """returns all values of layer."""
    layers = [theme, group, hashtag]

    if theme is None:
    # return all layers
    elif group is None:
    # return all groups for theme
    elif hashtag is None:


# return all tags for groups and theme


@database_v1.route("/themes/<theme>/groups/", methods=["POST"])
async def themes(request, theme, group, hashtag):
    """Post theme if it doesn't already exist.

    Parameters
    ----------
    theme : str
    group : str
    hashtag : str

    Returns
    -------
    dict
        saved theme
    """
    themes = ['Themes go here ']

    return json({'data': themes})


# this with GET
@database_v1.route("/themes/<theme>/groups/<group>/hashtags/<hashtag>", methods=["POST"])
async def themes(request, theme, group, hashtag):
    """Post theme if it doesn't already exist.

    Parameters
    ----------
    theme : str
    group : str
    hashtag : str

    Returns
    -------
    dict
        saved theme
    """
    themes = ['Themes go here ']

    return json({'data': themes})


@database_v1.route("/health", methods=["GET"])
async def posts(request):
    """Returns a list of themes.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    dict
        blueprint name
    """

    return json({'data': database_v1.name})
