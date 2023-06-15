#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = 0
        for key, val in a_dictionary.items():
            if val > max_score:
                max_score = val
                result = key
        return (result)
    return (None)
