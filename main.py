import requests
from bs4 import BeautifulSoup
import csv

from model import Product

def parser(url:str):
    create_csv()

    page = 1
    counter = 1

    while True:
        list_product = []
        res = requests.get(f'{url}/catalogue/page-{page}.html')
        soup = BeautifulSoup(res.text,"lxml")
        products = soup.find_all("article", class_="product_pod")
        for product in products:
            name = product.find("h3").find("a").get("title")
            price = product.find("p",class_="price_color").text[1:]
            availability = product.find("p",class_="instock availability").text.strip()
            rating = product.find("p").get("class")[1]
            urls = product.find("div",class_="image_container").find("a").get("href")
            if rating == "One":
                rating += " Star"
            else:
                rating += " Stars"
            list_product.append(Product(name=name,
                                        price=price,
                                        availability=availability,
                                        rating=rating,
                                        urls=urls))
            print(f'#{counter} {name} is done!')
            counter += 1
        write_csv(list_product)
        next_btn = soup.find("li",class_="next")
        if next_btn:
            page += 1
        else:
            break


def create_csv():
    with open("books.csv","w",newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([
            "name",
            "price",
            "availability",
            "rating",
            "urls"
        ])



def write_csv(products: list[Product]):
    with open("books.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([
                product.name,
                product.price,
                product.availability,
                product.rating,
                product.urls
            ])



if __name__ == "__main__":
    parser(url="https://books.toscrape.com/")