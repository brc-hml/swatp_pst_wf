from setuptools import setup, find_packages, Extension
import codecs
import os

# long description!!

# here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()
#

with open("README.rst", "r") as fd:
    long_desc = fd.read()


VERSION = '0.1.1'
DESCRIPTION = 'swatp_pst is a set of python modules for SWAT+ model evaluation and parameter estimation.'
# LONG_DESCRIPTION = 'A package that allows to work with SWAT-MODFLOW model'

license = "BSD-3-Clause"
# Setting up
setup(
    name="swatp_pst",
    version=VERSION,
    author="Seonggyu Park",
    author_email="<envpsg@gmail.com>",
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type="text/x-rst",
    download_url="https://pypi.org/project/swatp_pst",
    project_urls={
        "Bug Tracker": "https://github.com/spark-brc/swatp_pst/issues",
        "Source Code": "https://github.com/spark-brc/swatp_pst",
        "Documentation": "https://github.com/spark-brc/swatp_pst",
    },


    include_package_data=True,
    package_data = {
        'opt_files': ['*'],
    },
    packages=find_packages(),
    install_requires=[
        'pandas', 'numpy', 'scipy', 'matplotlib', 'openpyxl',
        'tqdm', 'termcolor', 'pyshp'],
    keywords=['python', 'SWAT+', 'PEST'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'Programming Language :: Python :: 3.10',
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: BSD License"
    ]
)