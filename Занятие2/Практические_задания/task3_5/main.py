wind = int(input())

# TODO напишите с помощью if-elif-else условие проверки скорости ветра
if wind in range (1, 5):
    print("Слабый")
elif wind in range (5, 11):
    print("Умеренный")
elif wind in range (11, 19):
    print("Сильный")
elif wind in range (19, 200):
    print("Ураганный")