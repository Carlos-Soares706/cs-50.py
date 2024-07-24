def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Confirmando quantos caracteres tem na placa
    if len(s) < 2 or len(s) > 6:
        return False

    # Verificando se os dois primeiros caracterees são letras usando a função "isalpha"
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # O primeiro numero não pode ser "0"
    for i in range(len(s)):
        if s[i].isalpha () == False:
            if s[i] == '0':
                return False
            else:
                break

    # A placa deve terminar com um numero
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # Não pode ter pontuação
    for i in s:
        if i in ['.', ' ', '?', '!']:
                 return False

    return True

if __name__ == "__main__":
    main()
