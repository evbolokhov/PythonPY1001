def factorial(n):
    f = 1

    # while n > 0:

     # f *= n
     # n -= 1
    # return f
    for i in range(1, n+1):
        f *= 1
    return f



if __name__ == "__main__":
    print(factorial(5))
