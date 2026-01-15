from typing import Any


def count_in_list(lst: list, check: Any) -> int:
    """
    counts the occurances of an object in a list
    """
    try:
        return lst.count(check)
    except AttributeError:
        print("AttributeError: argument is not a list")
        return 0
