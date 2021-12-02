a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a + c <= b or c + b <= a: #Учитывается то, что стороны не могут быть отрицательны или равны 0
    s = "Треугольника не существует"
else:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        s = "Прямоугольный"
    else:
        if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or c**2 + b**2 < a**2:
            s = "Тупоугольный"
        else:
            s = "Остроугольный"

if a + b > c and a + c > b and c + b > c:
    if  a == b == c:
        s += " равносторонний треугольник"
        print(s)
    else:
        if a == b or b == c or a == c:
            s += " равнобедренный треугольник"
            print(s)
        else:
            s += " произвольный треугольник"
            print(s)
else:
    print(s)