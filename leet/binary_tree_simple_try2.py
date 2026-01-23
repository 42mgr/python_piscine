array = [1, 3, 5, 7, 10, 15]
x = 10


def find_position(array: list[int], x: int) -> int:
    L = 0
    R = len(array) - 1

    while L <= R:
        M = L + (R - L) // 2
        if array[M] < x:
            L = M + 1
        elif array[M] > x:
            L = M - 1
        else:
            return M
    return -1


print(find_position(array, x))
