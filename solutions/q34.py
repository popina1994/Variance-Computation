import sys
import unittest


def knapsack_unbounded_values(values: list, weights: list, total_weight: int):
    a_max_values = [-sys.maxsize - 1] * (total_weight + 1)
    a_max_values[0] = 0
    for cur_weight in range(1, total_weight+1):
        for idx_weight, weight in enumerate(weights):
            if cur_weight - weight >= 0:
                    a_max_values[cur_weight] = max(a_max_values[cur_weight],
                                               a_max_values[cur_weight - weight] + values[idx_weight])

    print(a_max_values)
    return a_max_values


def knapsack_unbounded(values: list, weights: list, total_weight: int):
    a_max_values = knapsack_unbounded_values(values, weights, total_weight)
    return max(a_max_values)


def knapsack_unbounded_minimum_num_weights(weights: list, total_weight: int):
    values = [-1] * len(weights)
    knapsack_unbounded(values, weights, total_weight)
    a_max_values = knapsack_unbounded_values(values, weights, total_weight)
    return -a_max_values[total_weight]

def knapsack_unbounded_exact_weight(values: list, weights: list, total_weight: int):
    a_max_values = knapsack_unbounded_values(values, weights, total_weight)
    return a_max_values[total_weight]


def knapsack_zero_one_values(values: list, weights: list, total_weight: int):
    a_max_values = [-sys.maxsize - 1] * (total_weight + 1)
    a_max_values[0] = 0
    a_used_weights = []
    for i in range(total_weight + 1):
        a_used_weights.append([False] * len(weights))

    for cur_weight in range(1, total_weight+1):
        used_idx_weight = -1
        for idx_weight, weight in enumerate(weights):
            prev_weight = cur_weight - weight
            if (prev_weight >= 0) and not a_used_weights[prev_weight][idx_weight]:
                potential_value = a_max_values[prev_weight] + values[idx_weight]
                if potential_value > a_max_values[cur_weight]:
                    used_idx_weight = idx_weight
                    a_max_values[cur_weight] = potential_value
        if used_idx_weight != -1:
            weight = weights[used_idx_weight]
            prev_weight = cur_weight - weight
            for idx_weight in range(len(weights)):
                a_used_weights[cur_weight][idx_weight] = a_used_weights[prev_weight][idx_weight]
            a_used_weights[cur_weight][used_idx_weight] = True

    print(a_max_values)
    return a_max_values


def knapsack_zero_one(values: list, weights: list, total_weight: int):
    a_max_values = knapsack_zero_one_values(values, weights, total_weight)
    return max(a_max_values)


def knapsack_zero_one_exact(values: list, weights: list, total_weight: int):
    a_max_values = knapsack_zero_one_values(values, weights, total_weight)
    return a_max_values[total_weight]


class TestQuestion3(unittest.TestCase):
    def test_one(self):
        values = [10, 30, 20]
        weights = [5, 10, 15]
        total_weight = 100
        exp_value = 300
        self.assertEqual(knapsack_unbounded(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_unbounded_exact_weight(values, weights, total_weight), exp_value)

    def test_two(self):
        weights = [1, 2, 7]
        values = [10, 5, 8]
        total_weight = 7
        exp_value = 70
        self.assertEqual(knapsack_unbounded(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_unbounded_exact_weight(values, weights, total_weight), exp_value)

    def test_three(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        total_weight = 50
        exp_value = 300
        exp_value_zero_one = 220
        exp_value_min_weights = 2

        self.assertEqual(knapsack_unbounded(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_unbounded_exact_weight(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_zero_one_exact(values, weights, total_weight), exp_value_zero_one)
        self.assertEqual(knapsack_unbounded_minimum_num_weights(weights, total_weight), exp_value_min_weights)


    def test_paper(self):
        weights = [6, 3, 4, 2]
        values = [30, 14, 16, 9]
        total_weight = 10
        exp_value = 48
        exp_value_zero_one = 46
        exp_value_min_weights = 2
        self.assertEqual(knapsack_unbounded(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_unbounded_exact_weight(values, weights, total_weight), exp_value)
        self.assertEqual(knapsack_zero_one(values, weights, total_weight), exp_value_zero_one)
        self.assertEqual(knapsack_zero_one_exact(values, weights, total_weight), exp_value_zero_one)
        self.assertEqual(knapsack_unbounded_minimum_num_weights(weights, total_weight), exp_value_min_weights)

    def test_special(self):
        weights = [6, 4, 2, 2, 2]
        total_weight = 10
        exp_value_min_weights = 2
        self.assertEqual(knapsack_unbounded_minimum_num_weights(weights, total_weight), exp_value_min_weights)

if __name__ == '__main__':
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
