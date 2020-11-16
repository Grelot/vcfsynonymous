import setuptools

with open("doc/pypi_readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

     name='vcfsynonymous',  

     version='0.1.0',

     scripts=['src/demort.py'] ,

     author="Pierre-Edouard GUERIN",

     author_email="pierre-edouard.guerin@cefe.cnrs.fr",

     description="Detect synonymous genetic variants in VCF",

     long_description_content_type="text/markdown",

     long_description=long_description,
     

     url="https://github.com/Grelot/vcfsynonymous",

     packages=setuptools.find_packages(),

    install_requires=['argparse', 'numpy', 'biopython', 'bcbio-gff', 'pyfaidx', 'gffutils'],

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],
)