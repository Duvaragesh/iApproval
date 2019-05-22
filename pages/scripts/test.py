import sys

def main(foo, bar, *args):
    print("Called my script with")

    print("foo = %s" % foo)
    print("bar = %s" % bar)

    for arg in args:
        k = arg.split("=")[0]
        v = arg.split("=")[1]

        print "Keyword argument: %s = %s" % (k, v)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SyntaxError("Insufficient arguments.")
    if len(sys.argv) != 3:
        # If there are keyword arguments
        main(sys.argv[1], sys.argv[2], *sys.argv[3:])
    else:
        # If there are no keyword arguments
        main(sys.argv[1], sys.argv[2])