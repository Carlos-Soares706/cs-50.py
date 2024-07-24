texto = input("camelCase: ")

lista = []

for letra in texto:


    if not letra.isupper():
        lista.append(letra)
    else:
        lista.append('_' + letra.lower())

converted = ''.join(lista)

print(converted)

    #para cada letra no texto, verificar se a letra é maiuscula

