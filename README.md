# VCFSYNONYMOUS

[![PyPI version](https://badge.fury.io/py/vcfsynonymous.svg)](https://badge.fury.io/py/vcfsynonymous)
[![license](https://img.shields.io/pypi/l/vcfsynonymous.svg)](https://pypi.org/project/vcfsynonymous/)
[![Build Status](https://travis-ci.com/Grelot/vcfsynonymous.svg?branch=main)](https://travis-ci.com/Grelot/vcfsynonymous)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/vcfsynonymous.svg)](https://pypi.python.org/pypi/vcfsynonymous)



Giving `.gff3` and `.fasta` files of a genome and `.vcf` detected SNPs onto this genome, **VCFSYNONYMOUS** returns two `.vcf` files. The first one contains synonymous SNPs and the second one contains non-synonymous SNPs.


## INSTALLATION

```
pip3 install vcfsynonymous
```

## GET STARTED

```
vcfsynonymous --vcf tests/data/sample.vcf \
 --genome tests/data/genome.fasta \
 --annotation tests/data/genome.gff3
```


___________________________________________________________

## DEVELOPEMENT

### download dev version

```
git clone git@github.com:Grelot/vcfsynonymous.git
```

### test package

#### unit test

```
python -m pytest
```

#### real case test

```
python -m vcfsynonymous --vcf tests/data/sample.vcf \
 --genome tests/data/genome.fasta \
 --annotation tests/data/genome.gff3 \
 --output_prefix res
```

#### build package

```
pip3 uninstall vcfsynonymous
rm -rf build/
rm -rf dist/
rm -rf vcfsynonymous.egg-info/
python setup.py sdist bdist_wheel
```

local installation
```
pip3 install .
```

#### upload pypi

```
twine upload dist/*
```

pypi installation

```
pip install vcfsynonymous
```

#### uninstall 

```
pip uninstall vcfsynonymous
```
