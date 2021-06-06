# Autor: Carmen Lucía Arrabalí Cañete

import unittest
from src.main.Hamming import hamming

class HammingIT(unittest.TestCase):
    def setUp(self):
        self.hamming = hamming

    def test_Hamming_first(self):
        self.assertEqual(6, self.hamming('TGCCTTTACA', 'TGTAAAGGCA'))

    def test_Hamming_second(self):
        self.assertEqual(8, self.hamming('AAGGTTATGT', 'ACATAACCTT'))


if __name__ == '__main__':
    unittest.main()
