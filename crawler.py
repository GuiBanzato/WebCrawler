import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, filename):
    try:
        # Faz a solicitação HTTP para a URL
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação

        # Analisa o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrai todo o texto da página
        page_text = soup.get_text()

        # Salva o texto em um arquivo
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page_text)

        print(f"Informações extraídas e salvas em {filename}")
    
    except requests.RequestException as e:
        print(f"Ocorreu um erro na solicitação HTTP: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a página: {e}")

# Exemplo de uso
url = input("Insira o link da página: ")
filename = "output.txt"
scrape_and_save(url, filename)
