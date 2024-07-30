import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        full_links = [urljoin(url, link) for link in links]
        return full_links
    except requests.RequestException as e:
        print(f"Ocorreu um erro na solicitação HTTP: {e}")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao processar a página: {e}")
        return []

def scrape_and_save(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        page_text = soup.get_text()
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"\n\nURL: {url}\n")
            file.write(page_text)
        print(f"Informações extraídas de {url} e salvas em {filename}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro na solicitação HTTP: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a página: {e}")

def main():
    url = input("Insira o link da página principal: ")
    filename = "output.txt"

    links = get_all_links(url)
    print(f"Encontrados {len(links)} links na página principal.")

    for link in links:
        scrape_and_save(link, filename)

if __name__ == "__main__":
    main()
