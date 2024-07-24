import random

def main():
    level = get_level()  # Obtém o nível do usuário
    score = generate_integer(level)  # Gera problemas de matemática e retorna a pontuação
    print(score)  # Imprime a pontuação final

def get_level():
    # Loop para obter um nível válido
    while True:
        try:
            level = int(input("Level: "))  # Solicita ao usuário um nível de dificuldade
            if level >= 1 and level <= 3:  # Verifica se o nível está entre 1 e 3
                return level  # Retorna o nível válido
        except:
            pass  # Ignora entradas inválidas e continua solicitando

def generate_integer(level):
    score = 0  # Inicializa a pontuação

    for i in range(10):  # Gera 10 problemas de matemática
        # Gera números aleatórios dependendo do nível
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        attempts = 0  # Inicializa a contagem de tentativas para cada problema

        # Loop para permitir até 3 tentativas
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))  # Solicita a resposta do usuário

                if answer == x + y:  # Verifica se a resposta está correta
                    score += 1  # Incrementa a pontuação
                    break  # Sai do loop se a resposta estiver correta
                else:
                    attempts += 1  # Incrementa a contagem de tentativas
                    print("EEE")  # Informa que a resposta está incorreta

            except:
                attempts += 1  # Incrementa a contagem de tentativas em caso de erro de entrada
                print("EEE")  # Informa que a entrada foi inválida

        if attempts == 3:  # Se o usuário exceder as 3 tentativas
            print(f"{x} + {y} = {x + y}")  # Mostra a resposta correta

    return score  # Retorna a pontuação final

if __name__ == "__main__":
    main()  # Chama a função principal
