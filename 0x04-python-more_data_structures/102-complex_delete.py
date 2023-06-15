#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for key, val in a_dictionary.items():
        if val == value:
            key_list.append(key)
    for i in key_list:
        del a_dictionary[i]
    return (a_dictionary)
