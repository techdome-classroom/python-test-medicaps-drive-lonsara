class Solution(object):
    def romanToInt(s:str):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
    for char in reversed(s):
        value = roman_map[char]
        result += value if value >= prev_value else -value
        prev_value = value

    return result