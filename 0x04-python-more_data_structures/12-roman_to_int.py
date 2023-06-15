#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        new_str = roman_string[::-1]
        rom_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(new_str)):
            val = rom_num[new_str[i].upper()]
            if i == 0:
                result += val
            elif val < rom_num[new_str[i - 1].upper()] and i > 0:
                result -= val
            elif val >= rom_num[new_str[i - 1].upper()] and i > 0:
                result += val
        return (result)
    return (0)
