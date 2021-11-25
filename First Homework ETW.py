a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a + c <= b and c + b <= c:
    print("Треугольника не существует")
else:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print("Прямоугольный треугольник")
    else:
        if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or c**2 + b**2 < a**2:
            print("Остроугольный треугольник")
        else:
            print("Тупоугольный треугольник")
