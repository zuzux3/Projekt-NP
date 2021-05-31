def func(x, y):
    sum = x + y
    return sum


def Euler(x0, y0, xn, n):
    a = (xn - x0) / n

    print_str1 = '\n-----------------WYNIK----------------'
    print_str2 = '---------------------------------------'
    print_str3 = 'x0\ty0\tnachylenie\tyn'

    print(print_str1)
    print(print_str2)
    print(print_str3)
    print(print_str2)

    for i in range(n):
        nachylenie = func(xn, x0)
        yn = y0 + a * nachylenie
        print('%.2f\t %.2f\t %0.2f\t %.2f' % (x0, y0, nachylenie, yn))
        print(print_str2)

        y0 = yn
        x0 = x0 + a

    print('\nW x = %.2f, y = %.2f' % (xn, yn))


def Euler_Imp():
    enter_str1 = 'Wprowadz dane do obliczenia:\n'
    enter_str2 = 'Wprowadz punkt kalkulacji:\n'
    enter_str3 = 'Wprowadz liczbe krokow:\n'

    print(enter_str1)
    x0 = float(input('Podaj x0: '))
    y0 = float(input('Podaj y0: '))

    print(enter_str2)
    xn = float(input('Podaj xn: '))

    print(enter_str3)
    kroki = int(input('Podaj liczbe krokow: '))

    Euler(x0, y0, xn, kroki)
