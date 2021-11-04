def happiness(n):
    return print('Счастливое') if (sum([int(_) for _ in str(n)][:3])) == (sum([int(_) for _ in str(n)][3:])) else print('Не счастливое')


if __name__ == "__main__":
    N = 123321
    happiness(N)
