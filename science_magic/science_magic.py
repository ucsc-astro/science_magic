# from pkg_resources import resource_string
import os, inspect
from IPython.core.magic import (Magics, magics_class, line_magic)

@magics_class
class ScienceMagic(Magics):

    @line_magic
    def science(self, line):
        """Import statements"""
        from . import science_imports
        with open(inspect.getfile(science_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)
        self.astro(line)
        self.plotting(line)

    @line_magic
    def astro(self, line):
        """Import statements"""
        from . import astro_imports
        with open(inspect.getfile(astro_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

    @line_magic
    def plotting(self, line):
        """Import statements"""
        from . import plotting_imports
        with open(inspect.getfile(plotting_imports)) as f:
            s = f.read()
        ns = self.shell.user_ns
        print(s)
        exec(s, ns)

        if line is None:
            new_rc = {}
        else:
            new_rc = line
        install_dir = os.path.split(inspect.getfile(plotting_imports))[0]
        filename = install_dir + '/plotting_settings.txt'
        with open(filename) as f:
            s = f.read()
        s = s.format(new_rc.__str__())

        ns = self.shell.user_ns
        exec(s, ns)
