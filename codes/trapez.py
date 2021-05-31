def funkcja(x):
    return float(x) * float(x) + float(x) + 3


def trapez():
    n = float(input('Podaj ilosc trapezow: '))
    xp = input('Podaj poczatek przedzialu calkowania:  ')
    xk = input('Podaj koniec przedzialu calkowania:  ')
    dx = (float(xk) - float(xp)) / n
    print('Odległość między punktami podziałowymi: ' + str(dx))
    i = 1
    s = 0

    while i < n:
        s = s + (funkcja(float(xp) + float(i) * float(dx)))
        i = i+1

    s = ((s + (funkcja(xp) + funkcja(xk)) / 2) * dx)
    print('Całka: ')
    print('%.2f' % s)
