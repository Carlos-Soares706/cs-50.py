lista = {}

try:

    while True:
        item = input().upper()

        if item in lista:
            lista[item] += 1
        else:
            lista[item] = 1



except EOFError:


    for key in sorted(lista.keys()):
        print(lista[key], key)


