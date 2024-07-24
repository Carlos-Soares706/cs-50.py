import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Expressão regular para encontrar a tag iframe com a URL do YouTube
    iframe_match = re.search(r'<iframe[^>]*src="https://www\.youtube\.com/embed/([^"]+)"[^>]*></iframe>', s)

    if iframe_match:
        # Extraindo a parte da URL após 'embed/'
        video_id = iframe_match.group(1)
        return f"https://youtu.be/{video_id}"

    # Retorna None se não encontrar uma URL válida
    return None

if __name__ == "__main__":
    main()
