# What is the position of the value x?

array = [1, 3, 5, 10, 11, 15]
x = 10


def search_tree(array: list[int], x) -> int:
    L = 0
    R = len(array) - 1

    print(array)
    while L <= R:
        M = L + (R - L) // 2
        print(f"""L = {L}     M = {M}     R = {R}   array[M] = {array[M]}""")
        if array[M] < x:
            print("array[M] < x")
            L = M + 1
        elif array[M] > x:
            print("array[M] > x")
            R = M - 1
        elif array[M] == x:
            return M
        else:
            return -1
    return -2


def search_tree_flawed(array: list[int], x) -> int:
    L = 0
    R = len(array) - 1

    while L < R:
        M = (L + (R - L)) // 2
        print(f"""L = {L}     M = {M}     R = {R}   array[M] = {array[M]}""")
        if array[M] < x:
            print("array[M] < x")
            L = M
        elif array[M] > x:
            print("array[M] > x")
            R = M
        elif M == x:
            return M
        else:
            return -1
    return -2


print(search_tree(array, x))
