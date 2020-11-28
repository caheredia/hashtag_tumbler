from json import dump, load
from pathlib import Path

DATAPATH = "src/data"


def load_list(filepath: str, data_dir: str = DATAPATH) -> list:
    """Load list from JSON text file.

    filepath is assumed to be relative to data_dir.
    """
    with open(Path(data_dir, filepath)) as filehandler:
        loaded_list = load(filehandler)

    return loaded_list


chicano = load_list("chicano.txt")
film = load_list("film.txt")
fuji = load_list("fuji.txt")
leica = load_list("leica.txt")
mediumformat = load_list("mediumformat.txt")
sanfrancisco = load_list("sanfrancisco.txt")
street = load_list("street.txt")
