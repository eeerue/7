print('Дорогой друг! Эта программа предназначена для проверки того, сможет ли окружность радиуса R покрыть треугольник ABC. Если сможет, то программа выведет слово "покрывает", в противном случае - "0"')
print('Сторона a в труегольнике ABC =')
a = float(input())
print('Сторона b в труегольнике ABC =')
b = float(input())
print('Сторона c в труегольнике ABC =')
c = float(input())
print('Радиус окружности R =')
R = float(input())
if a+b>c and a+c>b and c+b>a:
    if R*2>=a or R*2>=b or R*2>=c:
        print('покрывает')
    else:
        print('0')
else:
    print('0')
