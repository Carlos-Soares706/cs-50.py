import random

# Loop para obter um nível válido
while True:
    try:
        level = int(input('Level: ')) # Solicita ao usuário um nível de dificuldade

        if level >= 1:
            rand_num = random.randint(1, level) # Gera um número aleatório entre 1 e o nível especificado
            break # Sai do loop uma vez que um nível válido é fornecido
    except:
        pass # Ignora entradas inválidas e continua solicitando


# Loop para adivinhar o número até acertar
while True:
    try:
        num_choice = int(input('Guess: ')) # Solicita ao usuário que adivinhe o número

        if num_choice > rand_num:
            print('Too large!') # Informa ao usuário que a adivinhação foi muito alta
        elif num_choice < rand_num:
            print('Too small!') # Informa ao usuário que a adivinhação foi muito baixa
        else:
            print('Just right!') # Informa ao usuário que acertou o número
            break # Sai do loop uma vez que o número correto é adivinhado

    except:
        pass # Ignora entradas inválidas e continua solicitando
