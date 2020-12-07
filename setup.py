import pathlib
from setuptools import find_packages, setup

README = ("README.md").read_text()


setup(

    name='vcfsynonymous',
    version='0.1.4',    
    author="Pierre-Edouard GUERIN",
    scripts=['vcfsynonymous/__main__.py'] ,
    author_email="pierre-edouard.guerin@cefe.cnrs.fr",
    description="Detect synonymous genetic variants in VCF",
    long_description=README,
    long_description_content_type="text/markdown",
    licence="MIT",
    url="https://github.com/Grelot/vcfsynonymous",
    packages=find_packages(),
    install_requires=['argparse', 'numpy', 'biopython', 'bcbio-gff', 'pyfaidx', 'gffutils', 'PyVCF'],

    classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ]
)