import setuptools

with open("doc/pypi_readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name='vcfsynonymous',
    version='0.1.1',
    scripts=['vcfsynonymous/__main.py__'] ,
    author="Pierre-Edouard GUERIN",
    author_email="pierre-edouard.guerin@cefe.cnrs.fr",
    description="Detect synonymous genetic variants in VCF",
    licence="MIT",
    url="https://github.com/Grelot/vcfsynonymous",
    packages=setuptools.find_packages(),
    install_requires=['argparse', 'numpy', 'biopython', 'bcbio-gff', 'pyfaidx', 'gffutils', 'PyVCF'],

    classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ]
)