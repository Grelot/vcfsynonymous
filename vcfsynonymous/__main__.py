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
from VariantCodon.objets import CdsSeq
from VariantCodon.dbfasta2CdsSeq import dbfasta2CdsSeq
from VariantCodon.synonymous import variant_position_within
from VariantCodon.synonymous import is_synonymous


#==============================================================================
#ARGUMENTS
#==============================================================================
if len(sys.argv) < 2:
    usage = """
 ____   ____   ______  ________  
|_  _| |_  _|.' ___  ||_   __  | 
  \ \   / / / .'   \_|  | |_ \_| 
   \ \ / /  | |         |  _|    
    \ ' /   \ `.___.'\ _| |_     
     \_/     `.____ .'|_____|    
 ___ _   _ _ __   ___  _ __  _ 59_, |_| |_| |_|\___/ \__,_|___/
     |___/                   |___/                           
                       
Pierre-Edouard GUERIN, Stephanie MANEL (CNRS, EPHE, Sorbonne University)
Founded by biodiversa RESERVEBENEFIT 2017-2020
version 0.0.1 "Haricot Dinde" november 2020

Usage:
> python3 vcfsynonymous [options]	
For help:
> python3 vcfsynonymous --help

	"""
    print(usage)
    sys.exit(0)

else:
    parser = argparse.ArgumentParser(description='VCFsynonymous - detect synonymous genetic variants in VCF')
    parser.add_argument("-f","--vcf", type=str, help='path of the variant Calling File (VCF) with variants you want to determine synonymous or non-synonymous')
    parser.add_argument("-g","--genome", type=str, help='path of the genome sequences FASTA file')
    parser.add_argument("-a","--annotation",type=str, help='path of the genome annotation GFF3 file')


#==============================================================================
#MAIN
#==============================================================================
## record arguments
args = parser.parse_args()
genomeFastaFile = args.genome
genomeGff3File = args.annotation
vcfFile = args.vcf


#genomeFastaFile = "data_test/genomes/sar_genome_lgt6000.fasta"
#vcfFile = "data_test/diplodus_sargus_exon.vcf"
#genomeGff3File = "data_test/annotation/DSARv1_annotation.gff3"
dbfnFile = 'currentgff.db'




## read GFF3 file
if os.path.exists(dbfnFile):
    os.remove(dbfnFile)
db = gffutils.create_db(genomeGff3File, dbfn=dbfnFile)
## read FASTA genome file
fasta = pyfaidx.Fasta(genomeFastaFile)
## From the genome(GFF3, FASTA),
cdsSeqList = dbfasta2CdsSeq(db, fasta)
## extract a list of CDS (coding sequences) objects
## read VCF file
vcf_reader = list(vcf.Reader(open(vcfFile, 'r')))
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






