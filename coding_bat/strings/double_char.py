"""
  Given a string, return a string where for every char in the original, there are two chars.
  double_char('The') → 'TThhee'
  double_char('AAbb') → 'AAAAbbbb'
  double_char('Hi-There') → 'HHii--TThheerree'
"""

def double_char(strings):
    result = ''
    for str in strings:
        result += str + str
    return result


def test(actual, expected):
    if actual == expected:
        result = 'CORRECT'
    else:
        result = 'WRONG'
    print(result)


test(double_char('The'), 'TThhee')
test(double_char('AAbb'), 'AAAAbbbb')
test(double_char('Hi-There'), 'HHii--TThheerree')
