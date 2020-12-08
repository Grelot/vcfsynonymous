import pathlib
from setuptools import find_packages, setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setup(
    name='vcfsynonymous',
    version='0.1.19',
    author="Pierre-Edouard GUERIN",    
    author_email="pierre-edouard.guerin@cefe.cnrs.fr",
    description="Detect synonymous genetic variants in VCF",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Grelot/vcfsynonymous",   
    packages=find_packages(),
    install_requires=['argparse', 'numpy', 'biopython', 'bcbio-gff', 'pyfaidx', 'gffutils', 'PyVCF'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
    ],
    entry_points={
    'console_scripts': [
        'vcfsynonymous=vcfsynonymous.__main__:main',
    ],
},  
)