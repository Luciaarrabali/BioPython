# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from src.main.K_Mers import k_mer

class K_MersIT(unittest.TestCase):
    def test_kmers_of_empty_sequence_should_be_empty(self):
        self.assertEqual([], k_mer('', 3))

    def test_3mers_of_a_sequence_should_be_correct(self):
        seq = 'ACGT'
        _3mers = ['ACG', 'CGT']
        self.assertEqual(_3mers, k_mer(seq, 3))


if __name__ == '__main__':
    unittest.main()
