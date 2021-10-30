if __name__ == "__main__":
    # Write your solution here
    a = 21345
    num_list = [int(x) for x in str(a)]

    print("1 ", num_list)
    print("2 ", sum(num_list))
    print("3 ", sum([x for x in num_list if x % 2 == 0]))
    print("4 ", len(num_list))
    print(f"5 min: {min(num_list)} max: {max(num_list)}")
    print("6н ", [x for x in num_list if num_list.index(x) % 2 == 0])
    print("6ч ", [x for x in num_list if num_list.index(x) % 2 != 0])
    print("7 ", str(num_list[0] - ) )
    print()