import requests
import sys

# Verifica se o número correto de argumentos foi fornecido
if len(sys.argv) == 2:
    try:
        # Tenta converter o argumento da linha de comando para um número float
        coin = float(sys.argv[1])
    except ValueError:
        # Imprime uma mensagem de erro se o argumento não for um número
        print("Command-line argument is not a number")
        sys.exit(1)  # Encerra o programa com um código de erro
else:
    # Imprime uma mensagem de erro se faltar o argumento da linha de comando
    print("Missing command-line argument")
    sys.exit(1)  # Encerra o programa com um código de erro

try:
    # Faz uma solicitação GET para a API do CoinDesk para obter o preço atual do Bitcoin
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # Converte a resposta para JSON
    resp = r.json()
    # Obtém a taxa de câmbio do Bitcoin em USD
    bitcoin = resp['bpi']['USD']['rate_float']
    # Calcula o valor da conta do usuário em dólares
    my_account = bitcoin * coin
    # Imprime o valor da conta formatado com 4 casas decimais
    print(f"${my_account:,.4f}")

except requests.RequestException:
    # Imprime uma mensagem de erro se houver uma exceção na solicitação
    print("RequestException")
    sys.exit(1)  # Encerra o programa com um código de erro

