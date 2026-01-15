import sys


def printEvenOddError(number: int):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    args = sys.argv[1:]

    try:
        assert (
            len(args) <= 1
        ), "AssertionError: more than one argument is provided"
        try:
            if len(args) == 1:
                printEvenOddError(int(args[0]))
        except ValueError:
            assert False, "AssertionError: argument is not an integer"

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    sys.exit(main())
