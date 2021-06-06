# Autor: Carmen Lucía Arrabalí Cañete

import unittest

from main.Rabbits import fibonacci

class RabbitsIT(unittest.TestCase):
    def setUp(self):
        self.fibonacci = fibonacci

    def test_rabbits_one_one(self):
        self.assertEqual(1, fibonacci(1))

    def test_rabbits_eight_five(self):
        self.assertEqual(8, fibonacci(5))

    def test_rabbits_10946_20(self):
        self.assertEqual(10946, fibonacci(20))


if __name__ == '__main__':
    unittest.main()
