import sys
import unittest


def matrix_multiplication_dynamic_programming(matrix_dims: list):
    d_opt_mat_mul_comp = {}
    for i in range(len(matrix_dims)):
        d_opt_mat_mul_comp[(i, i)] = 0

    print(matrix_dims)
    for window_size in range(2, len(matrix_dims) + 1):
        for idx_left in range(0, len(matrix_dims) - window_size + 1):
            idx_right = idx_left + window_size - 1
            d_opt_mat_mul_comp[(idx_left, idx_right)] = sys.maxsize
            for idx_mid in range(idx_left, idx_right):
                print(idx_left, idx_right, idx_mid)
                rec_mat_mul_comp = d_opt_mat_mul_comp[(idx_left, idx_mid)] + d_opt_mat_mul_comp[(idx_mid + 1, idx_right)]
                mat_mul_comp = rec_mat_mul_comp + \
                               matrix_dims[idx_left][0] * matrix_dims[idx_mid][1] * matrix_dims[idx_right][1]
                d_opt_mat_mul_comp[(idx_left, idx_right)] = min(d_opt_mat_mul_comp[(idx_left, idx_right)], mat_mul_comp)
    print(d_opt_mat_mul_comp)
    return d_opt_mat_mul_comp[(0, len(matrix_dims) - 1)]


class TestQuestion6(unittest.TestCase):
    def test_one(self):
        matrix_dims = [(10, 20), (20, 50), (50, 1), (1, 100)]
        exp_opt_comp = 2200
        self.assertEqual(matrix_multiplication_dynamic_programming(matrix_dims), exp_opt_comp)

    def test_two(self):
        matrix_dims = [(1, 2), (2, 3), (3, 4), (4, 3)]
        exp_opt_comp = 30
        self.assertEqual(matrix_multiplication_dynamic_programming(matrix_dims), exp_opt_comp)

    def test_three(self):
        matrix_dims = [(10, 20), (20, 30)]
        exp_opt_comp = 6000
        self.assertEqual(matrix_multiplication_dynamic_programming(matrix_dims), exp_opt_comp)

if __name__ == '__main__':
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
