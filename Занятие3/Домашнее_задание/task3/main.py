def long_word():
    a = input()
    b = a.split()
    n = (max(b, key=len))
    return n


if __name__ == "__main__":
    print(long_word())
