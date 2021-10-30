def some_func(lst):
    return[i ** 3 if i >= 0 else 0 i in lst]
if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(some_func(list_))