while True:


    fuel = input('Fraction: ')

    try:

        num,den = fuel.split('/')

        num_int = int(num)
        den_int = int(den)

        frac = num_int / den_int

        if frac <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

perc = round(frac * 100)

if perc <= 1:
    print(E)
elif perc >= 99:
    print('F')
else:
    print(f'{perc}%')
