def calcular_energia(massa):
    # Constante: velocidade da luz em metros por segundo
    c = 3e8  # 3 x 10^8 metros por segundo

    # Calcular a energia usando a fórmula E = mc^2
    energia = massa * c**2

    # Retornar a energia como um número inteiro
    return int(energia)

def main():
    # Solicitar ao usuário a massa em quilogramas
    massa = int(input("Digite a massa em quilogramas: "))

    # Calcular a energia equivalente
    energia_joules = calcular_energia(massa)


    print(f"{energia_joules}")

if __name__ == "__main__":
    main()
