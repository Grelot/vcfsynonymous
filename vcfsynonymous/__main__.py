#!/usr/bin/env python3
#===============================================================================
#INFORMATION
#===============================================================================
# Codes for vcfsynonymous 
# 
# CEFE - EPHE - RESERVEBENEFIT 2020
# Guerin Pierre-Edouard
#
# DEMORT evaluates demultiplexed fastq files by computing various metrics.
# DEMORT is a python3 program.
#
# git repository : https://github.com/Grelot/vcfsynonymous
#
#==============================================================================
#NOTICE
#==============================================================================
#
#concept:
#=======
#
#
#usage:
#=====
#>python3 vcfsynonymous --vcf vcfsynonymous/tests/data/sample.vcf \
# --genome vcfsynonymous/tests/data/genome.fasta \
# --annotation vcfsynonymous/tests/data/genome.gff3
#
#==============================================================================
#MODULES
#==============================================================================

## Standard library imports
import os
import sys
import argparse


## Third party imports (bioinformatics)
import gffutils
import pyfaidx
from Bio.Seq import Seq
import vcf

## Local applications import
from vcfsynonymous.objets import CdsSeq
from vcfsynonymous.objets import FileName
from vcfsynonymous.dbfasta2CdsSeq import dbfasta2CdsSeq
from vcfsynonymous.synonymous import variant_position_within
from vcfsynonymous.synonymous import is_synonymous
from vcfsynonymous.arguments import parse_args


#genomeFastaFile = "data_test/genomes/sar_genome_lgt6000.fasta"
#vcfFile = "data_test/diplodus_sargus_exon.vcf"
#genomeGff3File = "data_test/annotation/DSARv1_annotation.gff3"


def main():
    fichiers = parse_args()
    dbfnFile = 'currentgff.db'

    ## read GFF3 file
    if os.path.exists(dbfnFile):
        os.remove(dbfnFile)
    db = gffutils.create_db(fichiers.genomeAnnotation, dbfn=dbfnFile)
    ## read FASTA genome file
    fasta = pyfaidx.Fasta(fichiers.genomeFasta)
    ## From the genome(GFF3, FASTA),
    cdsSeqList = dbfasta2CdsSeq(db, fasta)
    ## extract a list of CDS (coding sequences) objects
    ## read VCF file
    vcf_reader = list(vcf.Reader(open(fichiers.vcf, 'r')))
    ## check wether variant is within a CDS
    for variant in vcf_reader:
        #print(variant.CHROM, variant.POS, variant.REF, variant.ALT[0])
        i=0
        for cdsSeq in cdsSeqList:        
            if variant_position_within(variant, cdsSeq):
                print("cds #", i)
                print(variant.CHROM,variant.POS, "|", cdsSeq.seqid, cdsSeq.start, cdsSeq.end)
                is_synonymous(variant, cdsSeq)
                break
            i+=1

if __name__ == '__main__':
    main()
