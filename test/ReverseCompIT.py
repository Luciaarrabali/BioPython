# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.ReverseCom import reverse_complement

class ReverseCompIT(unittest.TestCase):

    def setUp(self):
        self.reverseComplement = reverse_complement()

    def test_something(self):
        self.assertEqual('AGGAGTAAGA', self.reverseComplement('TCTTACTCCT'))


if __name__ == '__main__':
    unittest.main()
