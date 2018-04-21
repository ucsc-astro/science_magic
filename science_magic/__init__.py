from .science_magic import ScienceMagic


def load_ipython_extension(ipython):
    ipython.register_magics(ScienceMagic)

