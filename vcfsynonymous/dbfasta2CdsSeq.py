import gffutils
import pyfaidx
from vcfsynonymous.objets import CdsSeq


def dbfasta2CdsSeq(db, fasta):
    """
    From gff3 database (gffutils) and fasta genome sequence(pydaix)
    return a list of CdsSeq objects
    convert CDS sequences onto genome into CdsSeq object
    """
    cdsSeqList = []
    for cds in db.features_of_type(['CDS','cds']):
        #print(cds.sequence(fasta))
        #print(cds.seqid)
        #print(cds.start, cds.end)
        cdsSeq = cds.sequence(fasta)
        cdsSeqStartCodon = cdsSeq.find('ATG') #seek codon start ATG in the CDS 
        if(cdsSeqStartCodon != -1):
            cdsSeqID = cds.seqid
            cdsSeqStart = cdsSeqStartCodon+cds.start
            cdsSeqEnd = cds.end
            cdsSeqcoding = cdsSeq[cdsSeqStartCodon:]
            cdsSeqObj = CdsSeq(cdsSeqID, cdsSeqStart, cdsSeqEnd, cdsSeqcoding)
            cdsSeqList.append(cdsSeqObj)
    return(cdsSeqList)