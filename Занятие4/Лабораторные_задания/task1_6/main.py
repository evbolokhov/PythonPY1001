import random


def some_func(lst):
    print(lst)
    return len([x for x in lst if x > x > lst[0]])


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list1 = [random.randint(-10, 10) for _ in range(20)]
    print(some_func(list_))
    print(some_func(list1))
