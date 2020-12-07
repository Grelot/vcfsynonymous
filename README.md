# vcfsynonymous

[![PyPI version](https://badge.fury.io/py/vcfsynonymous.svg)](https://badge.fury.io/py/vcfsynonymous)
[![license](https://img.shields.io/pypi/l/vcfsynonymous.svg)](https://pypi.org/project/vcfsynonymous/)
[![Build Status](https://travis-ci.com/Grelot/vcfsynonymous.svg?branch=main)](https://travis-ci.com/Grelot/vcfsynonymous)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/vcfsynonymous.svg)](https://pypi.python.org/pypi/vcfsynonymous)



read VCF and select synonymous or non-synonymous coding variants



# Get started

```
python3 vcfsynonymous --vcf tests/data/sample.vcf \
 --genome tests/data/genome.fasta \
 --annotation tests/data/genome.gff3
```




# upload package

```
python setup.py sdist bdist_wheel
twine upload dist/*
```