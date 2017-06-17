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

    def test_vector_lt_error(self):
        list_low = [1, 0, 0]
        list_high = [1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        with self.assertRaises(TypeError):
            vector_low < vector_high

    def test_vector_lt_positive(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 1]

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

    def test_vector_sub(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 1]
        list_result = [0, 1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        vector_result = Vector.test(list_result)
        self.assertEqual(vector_high - vector_low, vector_result)

    def test_vector_sub_minus(self):
        list_low = [1, 0, 0]
        list_high = [1, 1, 1]
        list_result = [0, -1, -1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        vector_result = Vector.test(list_result)
        self.assertEqual(vector_low - vector_high, vector_result)


    def test_vector_neg_from_zero(self):
        list = [0, 0, 0]

        vector = Vector.test(list)
        self.assertEqual(vector, -vector)

    def test_vector_neg_from_negative(self):
        list = [-1, -1, -1]
        result_list = [1, 1, 1]

        vector = Vector.test(list)
        result = Vector.test(result_list)
        self.assertEqual(-vector, result)

    def test_vector_neg_from_positive(self):
        list = [1, 1, 1]
        result_list = [-1, -1, -1]

        vector = Vector.test(list)
        result = Vector.test(result_list)
        self.assertEqual(-vector, result)

    def test_vector_double_neg(self):
        list = [1, 1, 1]

        vector = Vector.test(list)
        self.assertEqual(-(-vector), vector)

    def test_vector_mul_right(self):
        list = [1, 1, 1]
        another_list = [-1, -1, -1]

        vector = Vector.test(list)
        another_vector = Vector.test(another_list)
        self.assertEqual(vector * another_vector, -3)

    def test_vector_mul_error(self):
        list = [1, 1, 1]
        another_list = [-1, -1]

        vector = Vector.test(list)
        another_vector = Vector.test(another_list)
        with self.assertRaises(TypeError):
            vector * another_vector

    def test_vector_sub_error(self):
        list_low = [1, 0, 0]
        list_high = [1, 1]

        vector_low = Vector.test(list_low)
        vector_high = Vector.test(list_high)
        with self.assertRaises(TypeError):
            vector_low - vector_high

if __name__ == '__main__':
    unittest.main()