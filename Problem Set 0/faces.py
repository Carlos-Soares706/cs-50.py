# faces.py

def convert(texto):
    """
    Esta função aceita uma string como entrada e retorna a mesma string
    com qualquer :) convertido para 🙂 e qualquer :( convertido para 🙁.
    """
    # Substitui :) por 🙂
    texto = texto.replace(":)", "🙂")
    # Substitui :( por 🙁
    texto = texto.replace(":(", "🙁")
    return texto

def main():
    """
    Esta função solicita ao usuário que insira um texto, chama a função convert
    com essa entrada e imprime o resultado.
    """
    # Solicita ao usuário que insira um texto
    entrada = input("Digite um texto: ")
    # Converte o texto inserido
    resultado = convert(entrada)
    # Imprime o resultado convertido
    print(resultado)

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
