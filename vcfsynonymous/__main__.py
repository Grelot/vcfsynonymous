
import argparse
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
import sys
import argparse


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
 ___ _   _ _ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ 
/ __| | | | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __|
\__ \ |_| | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \\
|___/\__, |_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/
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


import numpy
import biopython
from BCBio.GFF import GFFExaminer
from BCBio import GFF
import pprint


import gffutils
import pyfaidx
from Bio.Seq import Seq


genomeFastaFile = "data_test/genomes/sar_genome_lgt6000.fasta"

genomeGff3File = "data_test/annotation/DSARv1_annotation.gff3"

db = gffutils.create_db(genomeGff3File, dbfn='currentgff.db')
fasta = pyfaidx.Fasta(genomeFastaFile)

## decompose exon sequence into codon
for cds in db.features_of_type(['exon'], order_by='start'):
    cdsSeq = cds.sequence(fasta)
    frame=0
    cdsSeqStartCodon = cdsSeq.find('ATG')
    if(cdsSeqStartCodon != -1):
        print(cdsSeqStartCodon)
        coding = cdsSeq[cdsSeqStartCodon:]
        n = 3
        [coding[i:i+n] for i in range(0, len(coding), n)]
    else:
        frame+=1

print(frame)