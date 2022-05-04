def first():
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    c = int(input("Введите третье число:"))
    if a > b:
        print(a) if a > c else print(c)
    else:
        print(b) if b > c else print(c)


def second():
    b = 0
    z = int(input("Введите число z: "))
    x = int(input("Введите число x: "))
    c = int(input("Введите число c: "))
    q = int(input("Введите число q: "))
    w = int(input("Введите число w: "))
    lst = [z, x, c, q, w]
    for index in range(len(lst)):
        if lst[index] > 0:
            b += 1
    print(b)


def third():
     symbol = input("Введите тип символа ")
     if symbol.isdigit():
        print('Цифра')
     elif symbol.isalpha():
         print('Буква')
     else:
         print('Знак препинания')

def four():
    number = float(input("Введите число "))
    if number > 0 and int(number) == number:
        print('Натуральное')
    else:
        print('Не натуральное')

def five():
    a = int(input("Введите первую сторону: "))
    b = int(input("Введите вторую сторону: "))
    c = int(input("Введите третью сторону: "))
    if (a+b > c) and (a+c > b) and (c+b > a):
        print('да')
    else:
        print("Нет")

def six():
    while True:
        try:
            z = int(input("Введите номер билета: "))
            if len(str(z)) != 6:
                continue
        except ValueError:
            print("Ошибка")
        else:
            z = str(z)
            if int(z[0] + z[1] + z[2]) == int(z[3] + z[4] + z[5]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            elif int(z[0] == z[1] == z[2] == z[3] == z[4] == z[5]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            elif int(z[0] == z[5] and z[1] == z[4] and z[2] == z[3]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            else:
                print("Печалька, ваш билет:", z, " - несчаслтивый :(")
            break
