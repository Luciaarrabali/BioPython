# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.DNA import random_DNA

class DNAIT(unittest.TestCase):
    def setUp(self):
        self.randomDNA = random_DNA

    def test_dna_lenght_requested(self):
        self.assertEqual(3, len(random_DNA(3)))

    def test_only_ACGT(self):
        caracteres = ['A', 'C', 'G', 'T']
        DNArandom = random_DNA(10)
        matched_list = [nucleotide in caracteres for nucleotide in DNArandom]
        self.assertTrue(all(matched_list))


if __name__ == '__main__':
    unittest.main()
