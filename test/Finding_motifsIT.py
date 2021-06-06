# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.Finding_motifs import motifs
from collections import Counter


class Finding_motifsIT(unittest.TestCase):
    def setUp(self):
        self.FindingMotifs = motifs

    def test_Finding_motifs_one(self):
        self.assertEqual([('AG', 2), ('TT', 2)], motifs('TAGGTTTGAG'))


if __name__ == '__main__':
    unittest.main()
