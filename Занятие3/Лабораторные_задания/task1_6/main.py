def sum_(a, b):
    count =10
    b_ = 0
    wile count:
        b = b + b / 100 * 3
        b_ += b
        count -= 1
        return(b)
    else
        return(b*(((1.03)**10 - 1)/0.03))


if __name__ == "__main__":
    print(sum_(10000, 12000))
