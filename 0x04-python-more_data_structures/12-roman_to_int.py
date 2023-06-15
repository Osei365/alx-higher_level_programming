#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        rom_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(roman_string)-1):
            val = rom_num[roman_string[i]]
            if val < rom_num[roman_string[i + 1]]:
                result -= val
            result += val
        result += rom_num[roman_string[len(roman_string) - 1]]
        return (result)
    return (0)
