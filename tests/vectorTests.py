import unittest
from vector import *
from constants import *

class TestVectors(unittest.TestCase):
    def test_vector_creation(self):
        vector = Vector(3)
        self.assertEqual(vector.size, 3)

    def test_vector_creation_list(self):
        list = [i for i in range(10)]
        vector = Vector.test(list)
        self.assertEqual(vector.size, len(list))

        for i in list:
            self.assertEqual(vector.vectorData[i], list[i])

    def test_vector_generate(self):
        vector = Vector(3, True)
        self.assertEqual(vector.size, 3)

        for vectorNumber in vector.vectorData:
            self.assertEqual(type(vectorNumber), type(3))
            self.assertEqual(vectorNumber >= elemMinValue, True)
            self.assertEqual(vectorNumber <= elemMaxValue, True)

    def test_vector_gt_positive(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_high > vector_low, True)

    def test_vector_gt_negative(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_low > vector_high, False)

    def test_vector_gt_error(self):
        list_low = [1, 0, 0]
        list_high = [1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        with self.assertRaises(TypeError):
            vector_low > vector_high


    def test_vector_lt_negative(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_high < vector_low, False)

    def test_vector_lt_positive(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        with self.assertRaises(TypeError):
            vector_low < vector_high

    def test_vector_lt_error(self):
        list_low = [1, 0, 0]
        list_high = [1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_low < vector_high, True)

    def test_vector_eq_positive(self):
        list_low = [1, 0, 0]
        list_high = [1, 0, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_low == vector_high, True)

    def test_vector_eq_negative(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 0]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        self.assertEqual(vector_low == vector_high, False)

    def test_vector_eq_error(self):
        list_low = [1, 0, 0]
        list_high = [1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        with self.assertRaises(TypeError):
            vector_low == vector_high

if __name__ == '__main__':
    unittest.main()