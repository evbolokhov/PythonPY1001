def some_func(lst):
    even = len([x for x in lst if x % 2 == 0])
    odd = len([x for x in lst if x % 2 != 0])

    if even > odd:
        return "Chetnyh bolshe"
    elif even < odd:
        return "nech bolshe"
    return "ravno"


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    print(some_func(list_))
    print(some_func(range(1, 11)))
    print(some_func(range(1, 10)))
    print(some_func([2, 2, 2, 3]))
