def main():
    sqrt_list = []
    count = 0

    while sum(sqrt_list) < 500:
        sqrt_list.append(count ** 2)
        count += 1

    return len(sqrt_list) - 1


if __name__ == "__main__":
    print(main())
