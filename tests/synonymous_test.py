import sys
import os
import pickle
import unittest

from vcfsynonymous.VariantCodon.objets import CdsSeq
from vcfsynonymous.VariantCodon.synonymous import variant_position_within


class VariantCodonSynonymousTest(unittest.TestCase):
    """
    test case to check function from the submodule synonymous from the module VariantCodon    
    """
    def test_variant_position_within(self):
        vcf_reader = pickle.load( open( "tests/data/vcf_reader.pyObject", "rb" ) )
        cdsSeqList = pickle.load( open( "tests/data/cdsSeqList.pyObject", "rb" ) )        
        ## check variant outside intervals are not detected
        variant_within_no_cds = vcf_reader[7]
        cdsSeq_cds = cdsSeqList[2]
        assert variant_position_within(variant_within_no_cds, cdsSeq_cds) == 0
        ## check variant inside intervals are detected
        variant_within_cds=vcf_reader[0]
        assert variant_position_within(variant_within_cds, cdsSeq_cds) == 1



if __name__ == '__main__':
    unittest.main()
