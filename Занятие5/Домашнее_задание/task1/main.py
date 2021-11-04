if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, i + 1):
            k = i * j
            print("{0}*{1}={2}".format(i, j, k), end=" ")
        print("")