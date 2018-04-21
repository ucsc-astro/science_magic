from .science_magic import ScienceMagic

def load_ipython_extensions(ipython):
    ipython.register_magic_function(ScienceMagic)
