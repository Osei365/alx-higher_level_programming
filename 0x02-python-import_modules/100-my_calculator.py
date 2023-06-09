#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    av = sys.argv
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        n1 = int(av[1])
        n2 = int(av[3])
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(n1, n2, calc.add(n1, n2)))
        elif av[2] == '-':
            print("{} - {} = {}".format(n1, n2, calc.sub(n1, n2)))
        elif av[2] == '*':
            print("{} * {} = {}".format(n1, n2, calc.mul(n1, n2)))
        elif av[2] == '/':
            print("{} / {} = {}".format(n1, n2, calc.div(n1, n2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
