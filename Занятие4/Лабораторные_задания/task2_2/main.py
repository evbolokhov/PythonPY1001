if __name__ == "__main__":
    # Write your solution here
    a = 123489

    num_list = set([int(x) for x in str(a)])

    print(4 in num_list and  8 in num_list or 9 in num_list)
