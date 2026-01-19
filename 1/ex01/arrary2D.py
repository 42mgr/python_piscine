import numpy as np
import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    takes a 2D array of int/floats
    raises errors if this is not the case
    returns truncated version based on start and end lines
    """
    parsed = np.array(family)
    if parsed.ndim != 2:
        raise ValueError("input must be 2D array.")
    # check the kind of data: Integer i, Unsigned u, Float f -> iuf
    if parsed.dtype.kind not in "iuf":
        raise ValueError("only integers and floats are allowed as values")

    reshaped = parsed[start:end]

    print("My shape is : " + str(parsed.shape))
    print("My new shape is : " + str(reshaped.shape))

    return reshaped.tolist()


def main(family: list):
    try:
        user_input = input("Enter start and end: ")
        start, end = map(int, user_input.split())
        print(slice_me(family, start, end))
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    # Original from exercise
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    #
    # # Contains error: string
    # family = [[23, "a"], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    # # Contains error: 0 values
    # family = [
    #     [23, 0],
    #     [2.15, 0],
    #     [2.10, 0],
    #     [1.88, 0],
    # ]
    # # Contains error: unequal length (not a rectangle)
    # family = [[23, 78.4, 23.0], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    # # Contains error: wrong dimension
    # family = [
    #     [[23, 78.4], [23, 78.4]],
    #     [[23, 78.4], [23, 78.4]],
    #     [[23, 78.4], [23, 78.4]],
    # ]

    sys.exit(main(family))
