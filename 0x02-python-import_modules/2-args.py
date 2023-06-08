#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 1:
        print("{} argument:".format(lenth))
    elif length == 0:
        print("{} arguments.".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i + 1, argv[i + 1]))
