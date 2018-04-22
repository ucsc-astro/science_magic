from IPython.core.magic import (Magics, magics_class, line_magic)


@magics_class
class ScienceMagic(Magics):

    @line_magic
    def science(self, line):
        """Import statements"""
        s = """import numpy as np\nimport pandas as pd"""
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)
        self.astro(line)
        self.plotting(line)

    @line_magic
    def astro(self, line):
        """Import statements"""
        s = """from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.io import fits
from astropy import units as u
from astropy import constants as c"""
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

    @line_magic
    def plotting(self, line):
        s = """import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns"""
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

        if line is None:
            new_rc = {}
        else:
            new_rc = line
        s = """set_dict = dict(context='poster', style='ticks', font_scale=1.0, 
                               color_codes=True, palette='deep')
rc = {{'savefig.bbox': 'tight',
      'figure.figsize': (9, 6),
      'text.usetex': True,
      'image.origin': 'lower',
      'image.interpolation': 'none'}}
rc.update({})
print('matplotlib settings:')
for k, v in rc.items():
    print('\t{{}} = {{}}'.format(k, v))
print('seaborn settings:')
for k, v in set_dict.items():
    print('\t{{}} = {{}}'.format(k, v))
sns.set(rc=rc, **set_dict)
""".format(new_rc.__str__())
        ns = self.shell.user_ns
        exec(s, ns)
