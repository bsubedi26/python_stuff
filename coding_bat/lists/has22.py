"""
  Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
  has22([1, 2, 2]) → True
  has22([1, 2, 1, 2]) → False
  has22([2, 1, 2]) → False
"""

def has22(nums):
    try:
        for idx, n in enumerate(nums):
            if n == 2 and nums[idx + 1] == 2:
                return True

        return False
    except IndexError:
        return False


def test(actual, expected):
    if actual == expected:
        result = 'CORRECT'
    else:
        result = 'WRONG'
    print(result)


test(has22([1, 2, 2]), True)
test(has22([1, 2, 1, 2]), False)
test(has22([2, 1, 2]), False)
