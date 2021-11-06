if __name__ == "__main__":
    i = 15

    length = len(str(i**2)) + 3
    width = len(str(i)) + 3

    headers = " " * width + " " + "".join([str(j).rjust(length) for j in range(1, i + 1)])
    dashes = " " * width + ":" + "-" * length * i
    body = ""

    for row in range(1, i+1):
        body += str(row).rjust(width) + ":"
        for column in range(1, i+1):
            body += str(row * column).rjust(length)
        body += "\n"
    print("\n".join([headers, dashes, body]))
