
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


class CdsSeq:
    def __init__(self, seqid, start, end, sequence):
        self.seqid = seqid
        self.start = start
        self.end = end
        self.sequence = sequence
        self.codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]



def variant_position_within(coordsVar, coordsInterval):
    """
    check if coordsVars is within coordsInterval. Return 0
    """
    if coordsVar.CHROM == coordsInterval.seqid:
        if coordsVar.POS >= coordsInterval.start:
            if coordsVar.POS <= coordsInterval.end:
                return(1)
            else:
                return(0)
        else:
            return(0)
    return(0)


def is_synonymous(variant, cds):
    """
    check if a variant REF/ALT is synonymous or not from CDS codon in within it is located
    """
    posCodon = int((variant.POS - cds.start)/3) 
    codonVariant = cds.codons[posCodon]
    posVariantCodon = (variant.POS - cds.start)%3
    codonRef = list(codonVariant)
    codonAlt = list(codonVariant)
    codonRef[posVariantCodon] = str(variant.REF)
    codonAlt[posVariantCodon] = str(variant.ALT[0])
    codonRefSeq = Seq(''.join(codonRef))
    codonAltSeq = Seq(''.join(codonAlt))
    aaRef = str(codonRefSeq.translate(table=1))
    aaAlt = str(codonAltSeq.translate(table=1))
    print(codonVariant, "|||", codonRef, aaRef,"|", codonAlt, aaAlt)
    if aaRef != aaAlt:
        return(0)
    else:
        return(1)




import gffutils
import pyfaidx
from Bio.Seq import Seq
import vcf
import os

genomeFastaFile = "data_test/genomes/sar_genome_lgt6000.fasta"
vcfFile = "data_test/diplodus_sargus_exon.vcf"
genomeGff3File = "data_test/annotation/DSARv1_annotation.gff3"
dbfnFile = 'currentgff.db'



## read gff3 and fasta genome
if os.path.exists(dbfnFile):
    os.remove(dbfnFile)
db = gffutils.create_db(genomeGff3File, dbfn=dbfnFile)
fasta = pyfaidx.Fasta(genomeFastaFile)

## decompose exon sequence into codon
cdsSeqList = []
for cds in db.features_of_type(['CDS','cds'], order_by='start'):
    cdsSeq = cds.sequence(fasta)
    print(cds.seqid, cds.start, cds.end)
    cdsSeqStartCodon = cdsSeq.find('ATG')
    if(cdsSeqStartCodon != -1):
        cdsSeqID = cds.seqid
        cdsSeqStart = cdsSeqStartCodon+cds.start + cds.start
        cdsSeqEnd = cds.end       
        cdsSeqcoding = cdsSeq[cdsSeqStartCodon:]
        cdsSeqObj = CdsSeq(cdsSeqID, cdsSeqStart, cdsSeqEnd, cdsSeqcoding)
        cdsSeqList.append(cdsSeqObj)




## read vcf
vcf_reader = list(vcf.Reader(open(vcfFile, 'r')))

## check variant is within a cds
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






