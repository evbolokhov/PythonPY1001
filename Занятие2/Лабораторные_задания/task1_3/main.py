# TODO
a = int(input("A: "))
b = int(input("B: "))

if a * a + b * b == (a + b) * (a + b):
    print("равны")
elif  a * a + b * b > (a + b) * (a + b):
    print ("больше сумма квадратов")
else:
    print("больше квадрат суммы")
