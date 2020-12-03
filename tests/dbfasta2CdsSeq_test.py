import gffutils
import pyfaidx
from vcfsynonymous.VariantCodon.objets import CdsSeq

class VariantCodonTest(unittest.TestCase):
    """
    test case to check function from the module VariantCodon
    """

db = gffutils.FeatureDB("gff.db")
fasta = pyfaidx.Fasta("genome.fasta")