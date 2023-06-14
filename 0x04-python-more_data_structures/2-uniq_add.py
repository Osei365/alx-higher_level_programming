#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_res = 0
    for i in set(my_list):
        sum_res += i
    return (sum_res)
