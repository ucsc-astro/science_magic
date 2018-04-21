from setuptools import setup, find_packages

setup(
    name="science_magic",
    version=1.0,
    description="Import science!",
    author="Asher Wasserman",
    author_email="adwasser@ucsc.edu",
    url="https://github.com/adwasser/science_magic",
    license="MIT",
    packages=find_packages(exclude=[]),
    install_requires=[
        "numpy", "pandas", "astropy", "matplotlib", "seaborn", "ipython"
    ])
