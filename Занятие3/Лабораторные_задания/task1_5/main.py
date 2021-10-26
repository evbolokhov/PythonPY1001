def sum_list():
    i = int(input())
    lst = []

    while i != 0:
        if i > 0:
        lst.append(i)
        i = int(input())
    return sum(lst)

if __name__ == "__main__":
    print (sum_list())
