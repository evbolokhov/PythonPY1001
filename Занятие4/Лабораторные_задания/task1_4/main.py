def some_func(lst):
    average = sum(lst) / len(lst)
    print(average)
    return [x for x in lst ]
if __name__ == "__main__":
    # Write your solution here
    print(some_func(range(1, 9)))
    print(somefunc(range(3,5)))
    print(some_func(range(4, 14)))