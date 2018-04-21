from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

@magics_class
class ScienceMagic(Magics):

    @line_magic
    def science(self, line):
        """Import statements"""
        import numpy as np
        import pandas as pd
        print("""import numpy as np\nimport pandas as pd""")
        self.astro(line)
        self.plotting(line, None)

    @line_magic
    def astro(self, line):
        """Import statements"""
        from astropy.coordinates import SkyCoord
        from astropy.table import Table
        from astropy.io import fits
        from astropy import units as u
        from astropy import constants as c
        print("""from astropy.coordinates import SkyCoord
    from astropy.table import Table
    from astropy.io import fits
    from astropy import units as u
    from astropy import constants as c
    """)

    @cell_magic
    def plotting(self, line, cell):
        # updates rc params with contents of cell
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import seaborn as sns
        print("""import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns""")
        set_dict = dict(context='poster', style='ticks', font_scale=1.5,
                        color_code=True, palette='deep')
        rc={'savefig.bbox': 'tight',
            'figure.figsize': (9, 6),
            'text.usetex': True,
            'image.origin': 'lower',
            'image.interpolation': 'none'}
        rc.update(cell)
        print("matplotlib settings:")
        for k, v in rc.items():
            print("\t{} = {}".format(k, v))
        print("seaborn settings:")
        for k, v in set_dict.items():
            print("\t{} = {}".format(k, v))
        sns.set(rc=rc, **set_dict)



