# science_magic
IPython magic for importing science

It's like `%pylab` but with less littering of your namespace.

## Install
```shell
git clone git@github.com:ucsc-astro/science_magic.git
cd science_magic
pip install .
```
with the last line prepended by sudo for most python installations.

## Usage
You can make the new line magic commands automatically load as an IPython extension by adding the following to your `ipython_config.py` (usually located at `$HOME/.ipython/profile_default`):
```
c.InteractiveShellApp.extensions = ['science_magic']
```
Otherwise, you can load the extension manually with the magic command `%load_ext science_magic`.

`%science` does the following imports
```python
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.io import fits
from astropy import units as u
from astropy import constants as c
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
```

In addition, it sets up a default plotting enviroment with the following `matplotlib.rcParams` settings:
```
savefig.bbox = tight
figure.figsize = (9, 6)
text.usetex = True
image.origin = lower
image.interpolation = none
```
and the following seaborn settings:
```
context = poster
style = ticks
font_scale = 1.0
color_codes = True
palette = deep
```

`%astro` will just do the astropy imports, and `%plotting` will just do the matplotlib and seaborn imports.

You can pass a dictionary of rcParams settings as the line argument of either `%plotting` or `%science` (e.g., `%science {'errorbar.capsize': 2}` to update the default plotting settings.

## Customizing
Want to use this structure to set your own imports?  Don't like my default plotting settings? Just edit the relevant files under the `science_magic/science_magic` directory.  E.g., to add an import for `astropy.time.Time`, just add `from astropy.time import Time` to `science_magic/science_magic/astro_imports.py`.

