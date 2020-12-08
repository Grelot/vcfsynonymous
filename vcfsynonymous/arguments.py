import argparse
import sys

from vcfsynonymous.objets import FileName


HELPER_TEXT ="""
 ____   ____   ______  ________  
|_  _| |_  _|.' ___  ||_   __  | 
  \ \   / / / .'   \_|  | |_ \_|
   \ \ / /  | |         |  _|    
    \ ' /   \ `.___.'\ _| |_     
     \_/     `.____ .'|_____|    
                                                                      
  ___  _   _  _ __    ___   _ __   _   _  _ __ ___    ___   _   _  ___ 
 / __|| | | || '_ \  / _ \ | '_ \ | | | || '_ ` _ \  / _ \ | | | |/ __|
 \__ \| |_| || | | || (_) || | | || |_| || | | | | || (_) || |_| |\__ \\
 |___/ \__, ||_| |_| \___/ |_| |_| \__, ||_| |_| |_| \___/  \__,_||___/
        __/ |                       __/ |                              
       |___/                       |___/   


Pierre-Edouard GUERIN, Laura Benestan, Stephanie MANEL
CNRS, EPHE, Sorbonne University, Montpellier, France
Founded by biodiversa RESERVEBENEFIT 2017-2020
version 0.2 "Kidney Bean" november 2020

Usage:
> python3 vcfsynonymous [options]
For help:
> python3 vcfsynonymous --help

"""


def parse_args(usage=HELPER_TEXT):
    if len(sys.argv) < 2:       
        print(usage)
        sys.exit(0)
    else:
        parser = argparse.ArgumentParser(description='VCFsynonymous - detect synonymous genetic variants in VCF')
        parser.add_argument("-o","--output_prefix", type=str, help='prefix of the two output VCF files such as [PREFIX]_synonymous.vcf and [PREFIX]_nonsynonymous.vcf')
        parser.add_argument("-f","--vcf", type=str, help='path of the variant Calling File (VCF) with variants you want to determine synonymous or non-synonymous')
        parser.add_argument("-g","--genome", type=str, help='path of the genome sequences FASTA file')
        parser.add_argument("-a","--annotation",type=str, help='path of the genome annotation GFF3 file')
    args = parser.parse_args()
    fichiers = FileName(vcf =  args.vcf,
                        genomeFasta = args.genome,
                        genomeAnnotation = args.annotation,
                        outputPrefix = args.output_prefix)
    return fichiers
