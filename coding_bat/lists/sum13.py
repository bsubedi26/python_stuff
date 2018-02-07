"""
  Return the sum of the numbers in the array, returning 0 for an empty array.
  Except the number 13 is very unlucky, so it does not count and
  numbers that come immediately after a 13 also do not count.
  sum13([1, 2, 2, 1]) → 6
  sum13([1, 1]) → 2
  sum13([1, 2, 2, 1, 13]) → 6
"""

def thirteen_indxs(nums):
    indices = []
    for idx, n in enumerate(nums):
        if n == 13:
            indices.append(idx)

    return indices


def find_indices(nums):
    res = []
    indices = thirteen_indxs(nums)
    for n in indices:
        res.append(n)
        res.append(n + 1)

    return sorted(res, reverse=True)


def sum13(nums):
    res = []
    if len(nums) == 0:
        return 0

    if 13 not in nums:
        return sum(nums)

    idxs = find_indices(nums)
    for idx, n in enumerate(nums):
        if idx not in idxs:
            res.append(n)

    return sum(res)


def test(actual, expected):
    if actual == expected:
        result = 'CORRECT'
    else:
        result = 'WRONG'
    print(result)


test(sum13([1, 2, 2, 1]), 6)
test(sum13([1, 1]), 2)
test(sum13([1, 2, 2, 1, 13]), 6)
test(sum13([13, 1, 2, 13, 2, 1, 13]), 3)
test(sum13([]), 0)
test(sum13([5, 13, 2]), 5)
test(sum13([0]), 0)
test(sum13([13, 0]), 0)
