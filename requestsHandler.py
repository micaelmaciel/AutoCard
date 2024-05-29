import requests, time
from bs4 import BeautifulSoup

def get_page(url: str) -> BeautifulSoup:
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    }
    session = requests.Session()
    page = session.get(url, headers = headers)

    if page.status_code != 200:
        raise Exception(f"Status code is: {page.status_code}.\nReason: {page.reason}")
    
    return BeautifulSoup(page.content, "html.parser")

def get_sentences(word: str) -> list:
    baseQuery = "https://context.reverso.net/traducao/frances-portugues/"
    pageParsed = get_page(baseQuery + word)
    sentences = pageParsed.select('[lang="fr"]')
    sentencesList = []
    for i in sentences:
        senteceContent = ''.join(str(element) for element in i.contents).strip()
        sentencesList.append(senteceContent)

    return sentencesList

def get_word_data(word: str) -> tuple:
    time.sleep(1)
    baseQuery = "https://www.linguee.com.br/portugues-frances/search?source=auto&query="
    pageParsed = get_page(baseQuery + word)
    wordsUnparsed = pageParsed.select('.dictLink.featured')
    wordsParsed = [word.getText() for word in wordsUnparsed]
    baseWord = pageParsed.select_one('[class="dictLink"]').get_text(strip = True)

    return baseWord, wordsParsed

def main():
    baseQuery = "https://www.linguee.com.br/portugues-frances/search?source=frances&query="
    word = "vanter"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }

    session = requests.Session()
    page = session.get(baseQuery + word, headers = headers, stream = True)
    
    if page.status_code != 200:
        raise Exception("Returned status from server is", page.status_code, "Reason:", page.reason)
    
    pageParsed = BeautifulSoup(page.content, "html.parser")

    with open("response.html", "wb") as file:
        for chunk in page.iter_content(chunk_size = 1024):
            if chunk:
                file.write(chunk)
    
    sentences = pageParsed.select('.dictLink.featured')
    sentenceList = [s.get_text(strip=True) for s in sentences]
    
    print(sentenceList)

if __name__ == "__main__":
    main()
