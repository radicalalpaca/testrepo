import requests
from bs4 import BeautifulSoup

def get_links():
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    results_list = soup.find(id="results-list")
    books = results_list.find_all(class_="has-cover")
    links = []
    for book in books:
        title = book.find(class_="title")
        link = title.get("href")
        links.append(f"https://link.springer.com{link}")
    return links

def get_titles():
    titles = []
    for url in get_links():
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        evaluation_section = soup.find(class_="page-title")
        title = evaluation_section.find("h1").get_text()
        if "/" in title:
            formatted_title = title.replace("/", "_")
            titles.append(formatted_title.replace(" ", "_"))
        else:
            titles.append(title.replace(" ", "_"))
    return titles


def parse_links():
    links = []
    for url in get_links():
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        button_container = soup.find(class_="cta-button-container__item")
        book_container = button_container.find("a")
        link = book_container.get("href")
        links.append(f"https://link.springer.com{link}")
    return links

def save_pdf():
    counter = 0
    for link in parse_links():
        print(f"Downloading file: {get_titles()[counter]}.pdf")
        r = requests.get(link)
        with open(f"books/Math/{get_titles()[counter]}.pdf", "wb") as f:
            f.write(r.content)
        counter += 1

if __name__ == '__main__':
    urls = ["https://link.springer.com/search?facet-sub-discipline=%22Mathematical+Logic+and+Foundations%22&facet-content-type=%22Book%22&facet-language=%22En%22&facet-discipline=%22Philosophy%22&showAll=false&query="]
    for url in urls:
        get_links()
        get_links()
        parse_links()
        save_pdf()

