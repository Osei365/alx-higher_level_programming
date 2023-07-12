#!/usr/bin/python3
"""reads from stdin and prints out stats
after 10 metrics read."""


def print_stats(sz, codes):
    """Print after 10 metrics info.
    """

    print("File size: {}".format(sz))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    import sys

    sz = 0
    codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(sz, codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                sz += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if line[-2] not in codes.keys():
                        codes[line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(sz, codes)

    except KeyboardInterrupt:
        print_stats(sz, codes)
        raise
