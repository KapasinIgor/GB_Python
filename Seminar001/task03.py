# Задача №3

x = int(input("Введите x: "))
y = int(input("Введите y: "))

if (x == 0) and (y == 0):
    print("Это нулевая точка!")
elif (x > 0) and (y > 0):
    print("I четверть")
elif (x < 0) and (y > 0):
    print("II четверть")
elif (x < 0) and (y < 0):
    print("III четверть")
elif (x > 0) and (y < 0):
    print("IV четверть")