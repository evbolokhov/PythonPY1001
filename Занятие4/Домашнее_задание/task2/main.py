def equal_number(n):
    len__ = len([int(_) for _ in str(n)])
    len_ = len(set([int(_) for _ in str(n)]))
    return print('Есть одинаковые') if len_ != len__ else print('Нет одинаковых')


if __name__ == "__main__":
    N = input('Введите число: ')
    equal_number(N)
