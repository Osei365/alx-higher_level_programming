#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weighted_sum = 0
        count = 0
        for left, right in my_list:
            weighted_sum += (left * right)
            count += right
        return (weighted_sum/count)
    return (0)
