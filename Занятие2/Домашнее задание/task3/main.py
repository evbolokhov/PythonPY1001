if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    if ((A < 45) and (B >= 45) and (C >= 45)) or ((B < 45) and (C >= 45) and (A >= 45)) or ((C < 45) and (B >= 45) and (A >= 45)):
        print(True)
    else:
        print(False)
# TODO
