def equal_number(n):
    len_ = len(set([int(_) for _ in str(n)]))
    return print('true') if len_ == 1 else print('false')


if __name__ == "__main__":
    N = input('Введите число: ')
    equal_number(N)
