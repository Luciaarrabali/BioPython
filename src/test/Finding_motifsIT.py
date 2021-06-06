# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from src.main.Finding_motifs import motifs
from src.main.DNA import random_DNA


class Finding_motifsIT(unittest.TestCase):
    def test_motifs_of_empty_sequence_should_be_empty(self):
        self.assertEqual([], motifs('', 3))

    def test_number_of_results_parameter(self):
        seq = random_DNA(100)
        self.assertEqual(5, len(motifs(seq, 3, 5)))

    def test_motifs_count_should_be_correct(self):
        seq = 'ACACGACTAC'
        self.assertEqual([('AC', 4)], motifs(seq, 2, 1))


if __name__ == '__main__':
    unittest.main()
