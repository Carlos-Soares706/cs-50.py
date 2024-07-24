def calcular(expressão):
    sinais = ['+', '-', '*', '/']

    def achar_sinal(sinal, num1, num2):
        if sinal == '+':
            return num1 + num2
        elif sinal == '-':
            return num1 - num2
        elif sinal == '*':
            return num1 * num2
        elif sinal == '/':
            return num1 / num2

    simbolo = ''
    for sinal in sinais:
        if sinal in string:
            simbolo = sinal
            break

    if simbolo:
        numero1, numero2 = string.split(simbolo)
        numero1 = float(numero1.strip())
        numero2 = float(numero2.strip())
        resultado = achar_sinal(simbolo, numero1, numero2)
        return f'{resultado:.1f}'
    else:
        return "Operação inválida"

string = input("digitar a expressão: ")

print(calcular(string))
