#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        result = [i if i != search else replace for i in my_list]
        return (result)
    return (my_list)
