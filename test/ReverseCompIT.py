# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.ReverseCom import reverse_complement

class ReverseCompIT(unittest.TestCase):

    def setUp(self):
        self.reverseComplement = reverse_complement

    def test_something(self):
        self.assertEqual('CATTCCCTTA', self.reverseComplement('TAAGGGAATG'))

    def test_something(self):
        self.assertEqual('GGAGATCATT', self.reverseComplement('AATGATCTCC'))

    def test_something(self):
        self.assertEqual('GACGATTTGC', self.reverseComplement('GCAAATCGTC'))


if __name__ == '__main__':
    unittest.main()
