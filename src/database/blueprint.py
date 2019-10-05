from sanic import Blueprint
from sanic.response import json

database_v1 = Blueprint('database_v1', url_prefix='/database', version="v1")
database_v1.__doc__ = "database REST API"


@database_v1.route("/themes", methods=["GET"])
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
    list
        List of available themes
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
