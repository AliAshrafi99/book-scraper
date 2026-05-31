from camoufox.sync_api import Camoufox
import pandas as pd


def load_page(page):
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)


with Camoufox() as browser:
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")
    load_page(page)
    page.click("text=Historical")
    load_page(page)
    books = page.locator("article.product_pod").all()
    data = []
    for book in books:
        name = book.locator("h3 a").get_attribute("title")
        price = book.locator("p.price_color").inner_text()
        data.append({"name": name, "price": price})
        print(f"📚 {name} | 💰 {price}")

    df = pd.DataFrame(data)

    df.to_csv("books.csv", index=False, encoding="utf-8-sig")
    print("Data saved to books.csv")
    df.to_excel("books.xlsx", index=False)
    print("Data saved to books.xlsx")
