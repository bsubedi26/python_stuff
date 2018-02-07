"""
  Return the sum of the numbers in the array, except ignore sections
  of numbers starting with a 6 and extending to the next 7
  (every 6 will be followed by at least one 7). Return 0 for no numbers.

  sum67([1, 2, 2]) → 5
  sum67([1, 2, 2, 6, 99, 99, 7]) → 5
  sum67([1, 1, 6, 7, 2]) → 4
"""

def sum67(nums):
    if len(nums) == 0:
        return 0

    if 6 in nums and 7 in nums:
        index_6 = nums.index(6)
        index_7 = nums.index(7)

        res = nums[:index_6] + nums[index_7 + 1:]
        return sum(res)

    return sum(nums)


def test(actual, expected):
    if actual == expected:
        result = 'CORRECT'
    else:
        result = 'WRONG'
    print(result)


test(sum67([1, 2, 2]), 5)
test(sum67([1, 2, 2, 6, 99, 99, 7]), 5)
test(sum67([1, 1, 6, 7, 2]), 4)
