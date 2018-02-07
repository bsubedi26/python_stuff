"""
  Given an array length 1 or more of ints,
  return the difference between the largest and smallest values in the array.
  big_diff([10, 3, 5, 6]) → 7
  big_diff([7, 2, 10, 9]) → 8
  big_diff([2, 10, 7, 2]) → 8
"""

def big_diff(nums):
    max_num = max(nums)
    min_num = min(nums)
    return max_num - min_num


test(big_diff([10, 3, 5, 6]), 7)
test(big_diff([7, 2, 10, 9]), 8)
test(big_diff([2, 10, 7, 2]), 8)
