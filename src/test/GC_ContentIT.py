# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from src.main.GC_Content import gc_content

class GC_ContentIT(unittest.TestCase):
    def setUp(self):
        self.gc_content = gc_content

    def test_GC_Content_first(self):
        self.assertEqual(0.8, self.gc_content('GCGGGAGCGA'))

    def test_GC_Content_second(self):
        self.assertEqual(0.4, self.gc_content('TAATGAGTGC'))


if __name__ == '__main__':
    unittest.main()
