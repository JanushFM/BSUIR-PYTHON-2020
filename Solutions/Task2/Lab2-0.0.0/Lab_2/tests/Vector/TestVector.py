import unittest
from Lab_2.code.Vector.Vector import Vector
from math import sqrt


V1_LEN = sqrt(30)

NV1 = Vector([1, 2, 3, 4])

NV2 = Vector([5, 6, 7, 8])

NV3 = Vector([9, 10])
A = 3
V1_SUM_V2 = Vector([6, 8, 10, 12])
V1_SUB_V2 = Vector([-4, -4, -4, -4])
V1_MUL_A = Vector([3, 6, 9, 12])
V1_MUL_V2 = Vector([5, 12, 21, 32])


class TestVectorMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(NV1 + NV2, V1_SUM_V2)
        with self.assertRaises(Exception):
            NV1 + NV3
        with self.assertRaises(TypeError):
            NV1 + 3

    def test_sub(self):
        self.assertEqual(NV1 - NV2, V1_SUB_V2)
        with self.assertRaises(Exception):
            NV1 - NV3
        with self.assertRaises(TypeError):
            NV1 - 3

    def test_mul(self):
        self.assertEqual(NV1 * NV2, V1_MUL_V2)
        self.assertEqual(NV1 * A, V1_MUL_A)
        with self.assertRaises(TypeError):
            NV1 * "[1,2,3]"

    def test_eq(self):
        self.assertEqual(NV1 == NV2, False)
        self.assertEqual(NV1 == NV1, True)
        with self.assertRaises(TypeError):
            NV1 == 15
        with self.assertRaises(Exception):
            NV1 == NV3

    def test_len(self):
        self.assertAlmostEqual(NV1.__len__(), V1_LEN, delta=0.02)

    def test_get(self):
        self.assertEqual(NV1[2], 3)
        with self.assertRaises(IndexError):
            NV1[6]


if __name__ == '__main__':
    unittest.main()
