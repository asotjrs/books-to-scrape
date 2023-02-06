import requests
from bs4 import BeautifulSoup
book_list=[]

try:


    for x in range(1,51):
        print(x)
        url = f"https://books.toscrape.com/catalogue/page-{x}.html"

        response = requests.get(url,timeout=1000000)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features="html.parser")
        articles = soup.findAll("article", class_="product_pod")

        for book in articles:
            title = book.find_all("a")[1].text
            price = book.find("p", class_="price_color").text[2:]
            instock = book.find("p", class_="instock availability").text.strip()
            book_list.append({
                'title': title,
                'price': price,
                'instock': instock
            })
    print(book_list[5])  # for example
except requests.exceptions.Timeout as e:
    print("The request timed out")
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)
except requests.exceptions.RequestException as e:
    print("An error occurred during requests:", e)
