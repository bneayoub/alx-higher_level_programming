#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    av = sys.argv[2]
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if av not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{0} {1} {2} = {3}".format(a, av, b, operator[av](a, b)))
