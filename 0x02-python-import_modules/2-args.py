#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 2:
        print("{} argument:".format(l - 1))
    elif length > 2:
        print("{} arguments:".format(l - 1))
    else:
        print("{} arguments.".format(l - 1))
    for i in range(len(argv[1:])):
        print("{}: {}".format(i + 1, argv[i + 1]))
