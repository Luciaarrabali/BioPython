# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.GC_Content import gc_content

class GC_ContentIT(unittest.TestCase):
    def setUp(self):
        self.gc_content = gc_content()

    def test_GC_Content_first(self):
        self.assertEqual(0.42, self.gc_content('TCGAACACTGGATGTTGATAAATTTGCTTTGCACCATCTGCCAGCATCAA'))

    def test_GC_Content_second(self):
        self.assertEqual(0.56, self.gc_content('GATGGTACCGTCAAACCTTCTGCACAGCGTGTCCGCCTCTTGAAGCAGGT'))


if __name__ == '__main__':
    unittest.main()
