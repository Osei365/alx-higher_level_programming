#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            val_count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (val_count)
