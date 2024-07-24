def main():
    # Dicionário de extensões de arquivo e seus tipos de mídia correspondentes
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Solicitar ao usuário o nome do arquivo
    filename = input("File name: ").strip().lower()

    # Obter a extensão do arquivo
    if '.' in filename:
        ext = '.' + filename.split('.')[-1]
    else:
        ext = ''

    # Determinar o tipo de mídia com base na extensão
    media_type = media_types.get(ext, "application/octet-stream")

    # Exibir o tipo de mídia
    print(media_type)

if __name__ == "__main__":
    main()
