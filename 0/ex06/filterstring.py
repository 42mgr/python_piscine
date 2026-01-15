import sys

from ft_filter import ft_filter


def main():
    """takes two arguments:
        - string
        - integer
    outputs all strings > integer
    """
    text = ""
    length = 0

    args = sys.argv[1:]
    try:
        match args:

            case [string, int_string] if isinstance(string, str):
                text = string.split()
                length = int(int_string)
                # lambda
                print(list(ft_filter(lambda x: (len(x) > length), text)))
            case _:
                raise AssertionError

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return 1


if __name__ == "__main__":
    sys.exit(main())
