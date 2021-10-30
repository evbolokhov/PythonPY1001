def some_func(lst):
    average = sum(lst) / len(lst)
    print(average)
    return [round(x - average, 2) for x in lst]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(some_func(list_))
