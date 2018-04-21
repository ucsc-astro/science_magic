from setuptools import setup

setup(
    name="science_magic",
    version=1.0,
    description="Import science!",
    author="Asher Wasserman",
    author_email="adwasser@ucsc.edu",
    license="MIT",
    packages=["science_magic"],
    install_requires=[
        "numpy", "pandas", "astropy", "matplotlib", "seaborn"
    ],
    include_package_data=True)

