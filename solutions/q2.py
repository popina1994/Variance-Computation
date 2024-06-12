import unittest


def maximum_cont_sub_sum_brute_force(l: list) -> list:
    if (l is None) or (len(l) == 0):
        return []
    len_l = len(l)

    max_idx_left = -1
    max_idx_right = -1
    max_sum = 0
    for idx_left in range(0, len_l):
        for idx_right in range(idx_left, len_l):
            sum_val = sum(l[idx_left:(idx_right+1)])
            if sum_val > max_sum:
                max_idx_left = idx_left
                max_idx_right = idx_right
                max_sum = sum_val

    if max_sum == 0:
        return []
    return l[max_idx_left:(max_idx_right+1)]


def maximum_cont_sub_sum_optimized(l: list) -> list:
    if (l is None) or (len(l) == 0):
        return []
    len_l = len(l)

    pref_sum = [0] * len_l
    pref_sum[0] = l[0]
    for idx in range(1, len_l):
        pref_sum[idx] = pref_sum[idx-1] + l[idx]

    a_max_cont_sub_sums = [0] * len_l
    max_idx_left = -1
    max_idx_right = -1
    max_sum = 0
    for idx_left in range(0, len_l):
        for idx_right in range(idx_left, len_l):
            if idx_left > 0:
                pref_sum_left = pref_sum[idx_left-1]
            else:
                pref_sum_left = 0
            sum_val = pref_sum[idx_right] - pref_sum_left

            if sum_val > max_sum:
                max_idx_left = idx_left
                max_idx_right = idx_right
                max_sum = sum_val

    if max_sum == 0:
        return []

    return l[max_idx_left:(max_idx_right + 1)]


def maximum_cont_sub_sum_dyn_progr(l: list) -> list:
    if (l is None) or (len(l) == 0):
        return []
    len_l = len(l)

    idx_left = 0
    idx_right = -1

    max_idx_left = -1
    max_idx_right = -1
    max_sum = 0

    a_max_cont_sub_sums = [0] * len_l
    a_idx_lefts = [-1] * len_l
    if l[0] > 0:
        a_max_cont_sub_sums[0] = l[0]
        a_idx_lefts[0] = 0


    for idx in range(1, len_l):
        if a_max_cont_sub_sums[idx-1] + l[idx] > 0:
            a_max_cont_sub_sums[idx] = a_max_cont_sub_sums[idx - 1] + l[idx]
            a_idx_lefts[idx] = idx_left
        else:
            a_max_cont_sub_sums[idx] = 0
            idx_left = idx + 1
            a_idx_lefts[idx] = -1

    print("idx_lefts", a_idx_lefts)
    print("a_max_cont_sub_sums", a_max_cont_sub_sums)

    for idx in range(len_l):
        if a_max_cont_sub_sums[idx] > max_sum:
            max_idx_left = a_idx_lefts[idx]
            max_idx_right = idx
            max_sum = a_max_cont_sub_sums[idx]
    if max_sum == 0:
        return []

    return l[max_idx_left:(max_idx_right+1)]


class TestQuestion1(unittest.TestCase):
    def test_empty(self):
        input_list = []
        exp_list = []
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)

    def test_none(self):
        input_list = None
        exp_list = []
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)

    def test_example(self):
        input_list = [1, 2, 3, -11, 10, 6, -10, 11, -5]
        exp_list = [10, 6, -10, 11]
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)

    def test_example2(self):
        input_list = [1, 2, 3, -11, 10]
        exp_list = [10]
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)


    def test_example3(self):
        input_list = [1, 2, 3, -11, -12, -4, 4]
        exp_list = [1, 2, 3]
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)


    def test_example4(self):
        input_list = [1, 2, 3, -11, -12, -4, 4, -7, 8, 9]
        exp_list = [8, 9]
        self.assertEqual(maximum_cont_sub_sum_brute_force(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_optimized(input_list), exp_list)
        self.assertEqual(maximum_cont_sub_sum_dyn_progr(input_list), exp_list)

if __name__ == '__main__':
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
