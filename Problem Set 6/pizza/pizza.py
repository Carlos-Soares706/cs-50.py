import sys
import csv
from tabulate import tabulate

def main():
    # Verifica os argumentos de linha de comando
    check_command()

    table = []

    try:
        # Tenta abrir o arquivo CSV fornecido como argumento de linha de comando
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            # Lê todas as linhas do arquivo e adiciona à tabela
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, exibe uma mensagem de erro e sai
        sys.exit('File does not exist')

    # Usa a função tabulate para formatar a tabela como uma grade
    tabul = tabulate(table, headers='firstrow', tablefmt='grid')

    # Imprime a tabela formatada
    print(tabul)

def check_command():
    len_argv = len(sys.argv)

    # Verifica se há argumentos de linha de comando suficientes
    if len_argv < 2:
        sys.exit("Too few command-line arguments")

    # Verifica se há muitos argumentos de linha de comando
    if len_argv > 2:
        sys.exit("Too many command-line arguments")

    # Verifica se o argumento fornecido é um arquivo CSV
    if not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
