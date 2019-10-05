def get_rows(theme=None, groups=None, hashtags=None):
    """Returns a list of dictionary itemsk depending on the layer

    Parameters
    ----------
    theme: str

    groups: str

    hashtags: str

    RETURNS
    -------
    data: dict
        retrieved data from database
    """

    url_suffix = f"/cells/tables/{table}"
    if row is not None:
        url_suffix = f"/cells/tables/{table}/rows/{row}"
    if family is not None:
        url_suffix = f"/cells/tables/{table}/rows/{row}/families/{family}"
    if (family is not None) and (qualifier is not None):
        url_suffix = f"/cells/tables/{table}/rows/{row}/families/{family}/qualifiers/{qualifier}"

    r = requests.get(DATABASE_API_URL + DATABASE_PREFIX + url_suffix, headers=headers)

    cells = r.json()['data']
    return cells
