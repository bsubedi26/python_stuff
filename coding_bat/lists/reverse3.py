def reverse3(nums):
    result = []
    length = len(nums) - 1

    for n in nums:
        result.append(nums[length])
        length -= 1

    return result


def test(actual, expected):
    if actual == expected:
        result = 'CORRECT'
    else:
        result = 'WRONG'
    print(result)


test(reverse3([1, 2, 3]), [3, 2, 1])
test(reverse3([5, 11, 9]), [9, 11, 5])
test(reverse3([7, 0, 0]), [0, 0, 7])
