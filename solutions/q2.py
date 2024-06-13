import unittest


def print_edit_matrix(ed_dist_mat, str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    print("%3c" % "-", end='')
    print("%3c" % "-", end='')
    for idx_b in range(0, len_b):
        print("%3c" % str_b[idx_b], end='')
    print()
    for idx_a in range(0, len_a + 1):
        if idx_a == 0:
            print("%3c" % "-", end='')
        else:
            print("%3c" % str_a[idx_a - 1], end='')
        for idx_b in range(0, len_b + 1):
            print("%3d" % ed_dist_mat[idx_a][idx_b], end='')
        print("")
    print("")


def back_track_changes(ed_dist_matrix, str_a, str_b):
    idx_a = len(str_a)
    idx_b = len(str_b)
    changes = []
    cur_idx = ed_dist_matrix[idx_a][idx_b]

    while not (idx_a == 0 and idx_b == 0):
        if idx_a == 0:
            changes.append(('I', idx_b, str_b[idx_b-1]))
            idx_b -= 1
        elif idx_b == 0:
            changes.append(('D', 0))
            idx_a -= 1
        else:
            if str_a[idx_a-1] == str_b[idx_b-1]:
                idx_a = idx_a - 1
                idx_b = idx_b - 1
            else:
                if ed_dist_matrix[idx_a - 1][idx_b] + 1 == ed_dist_matrix[idx_a][idx_b]:
                    change = ('D', idx_b)
                    idx_a = idx_a - 1
                else:
                    change = ('I', idx_b-1, str_b[idx_b-1])
                    idx_b = idx_b - 1
                changes.append(change)
        print("Backtracking position", idx_a, idx_b)
    changes.reverse()

    return changes


def edit_distance(str_a: str, str_b: str) -> int:
    len_a = len(str_a)
    len_b = len(str_b)

    ed_dist_mat = []

    # Allocate the distance matrix
    for idx_a in range(len_a + 1):
        ed_dist_mat.append([0] * (len_b+1))

    # Initialize the edge cases of the distance matrix
    for idx_a in range(len_a+1):
        ed_dist_mat[idx_a][0] = idx_a
    for idx_b in range(len_b+1):
        ed_dist_mat[0][idx_b] = idx_b

    for idx_a in range(1, len_a+1):
        for idx_b in range(1, len_b+1):
            if str_a[idx_a-1] == str_b[idx_b-1]:
                ed_dist_mat[idx_a][idx_b] = ed_dist_mat[idx_a-1][idx_b-1]
            else:
                ed_dist_mat[idx_a][idx_b] = min(ed_dist_mat[idx_a-1][idx_b], ed_dist_mat[idx_a][idx_b-1]) + 1

    print_edit_matrix(ed_dist_mat, str_a, str_b)
    changes = back_track_changes(ed_dist_mat, str_a, str_b)
    print(changes)

    tran_str = str_a
    print("Original:", tran_str)
    for change in changes:
        if change[0] == 'D':
            del_pos = change[1]
            print("Deleting the letter", tran_str[del_pos], "at the position", del_pos)
            tran_str = tran_str[:del_pos] + tran_str[(del_pos+1):]
        elif change[0] == 'I':
            ins_pos = change[1]
            char_letter = change[2]
            print("Inserting the letter", char_letter, "at the position", ins_pos)
            prefix = tran_str[:ins_pos]
            suffix = tran_str[ins_pos:]
            prefix = "" if len(prefix) == 0 else prefix
            suffix = "" if len(suffix) == 0 else suffix
            tran_str = prefix + char_letter + suffix
        print("After transformation", tran_str)

    return ed_dist_mat[len_a][len_b]


class TestQuestion2(unittest.TestCase):
    def test_empty(self):
        str_a = []
        str_b = []
        exp_num = 0
        self.assertEqual(edit_distance(str_a, str_b), exp_num)

    def test_one_empty_other_full(self):
        str_a = []
        str_b = "0123456789"
        exp_num = 10
        self.assertEqual(edit_distance(str_a, str_b), exp_num)

    def test_example(self):
        str_a = "cheese"
        str_b = "chess"
        exp_num = 3
        self.assertEqual(edit_distance(str_a, str_b), exp_num)

    def test_example2(self):
        str_a = "rhymes"
        str_b = "reason"
        exp_num = 6
        self.assertEqual(edit_distance(str_a, str_b), exp_num)


if __name__ == '__main__':
    print("HELLO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
