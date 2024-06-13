import sys
import unittest


def is_palindrome(s_str: str) -> bool:
    len_s = len(s_str)
    for idx in range(len_s // 2):
        if s_str[idx] != s_str[len_s - idx - 1]:
            return False

    return True


def palindrome_brute_force(s_str: str):
    max_len_palindrome = 0
    for idx_left in range(0, len(s_str)):
        for idx_right in range(idx_left, len(s_str)):
            if is_palindrome(s_str[idx_left:(idx_right+1)]):
                max_len_palindrome = max(idx_right - idx_left + 1, max_len_palindrome)

    return max_len_palindrome


def palindrome_dynamic_programming(s_str: str):
    d_max_palindrome_len = {}
    for i in range(len(s_str)):
        d_max_palindrome_len[(i, i)] = 1

    for window_size in range(2, len(s_str) + 1):
        for idx_left in range(0, len(s_str) - window_size + 1):
            idx_right = idx_left + window_size - 1
            pot_max_len = d_max_palindrome_len[(idx_left + 1, idx_right - 1)] if idx_left + 1 <= idx_right - 1 else 0

            if s_str[idx_left] == s_str[idx_right]:
                pot_max_len += 2
            d_max_palindrome_len[(idx_left, idx_right)] = max(d_max_palindrome_len[(idx_left + 1, idx_right)],
                                                                 d_max_palindrome_len[(idx_left, idx_right - 1)],
                                                                 pot_max_len)
    return d_max_palindrome_len[(0, len(s_str) - 1)]


class TestQuestion3(unittest.TestCase):
    def test_one(self):
        s_str = "abc"
        exp_palindrome_len = 1
        self.assertEqual(palindrome_brute_force(s_str), exp_palindrome_len)
        self.assertEqual(palindrome_dynamic_programming(s_str), exp_palindrome_len)

    def test_two(self):
        s_str = "aba"
        exp_palindrome_len = 3
        self.assertEqual(palindrome_brute_force(s_str), exp_palindrome_len)
        self.assertEqual(palindrome_dynamic_programming(s_str), exp_palindrome_len)

    def test_three(self):
        s_str = "abb"
        exp_palindrome_len = 2
        # self.assertEqual(palindrome_brute_force(s_str), exp_palindrome_len)
        self.assertEqual(palindrome_dynamic_programming(s_str), exp_palindrome_len)


    def test_four(self):
        s_str = "abcabccbaaa"
        exp_palindrome_len_con = 6
        exp_palindrome_len = 8
        self.assertEqual(palindrome_brute_force(s_str), exp_palindrome_len_con)
        self.assertEqual(palindrome_dynamic_programming(s_str), exp_palindrome_len)

    def test_five(self):
        s_str = "BBABCBCAB"
        exp_palindrome_len_con = 3
        exp_palindrome_len = 7
        self.assertEqual(palindrome_brute_force(s_str), exp_palindrome_len_con)
        self.assertEqual(palindrome_dynamic_programming(s_str), exp_palindrome_len)


if __name__ == '__main__':
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
