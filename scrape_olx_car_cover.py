import requests
from bs4 import BeautifulSoup

def scrape_olx_car_cover():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("li", {"data-aut-id": "itemBox"})

    results = []
    for item in items:
        title = item.find("span", {"data-aut-id": "itemTitle"})
        price = item.find("span", {"data-aut-id": "itemPrice"})
        location = item.find("span", {"data-aut-id": "itemLocation"})
        link = item.find("a", href=True)

        if title and price and location and link:
            results.append({
                "title": title.text.strip(),
                "price": price.text.strip(),
                "location": location.text.strip(),
                "link": link['href'].strip()
            })

    with open("olx_car_cover_results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(f"Title: {r['title']}\nPrice: {r['price']}\nLocation: {r['location']}\nLink: {r['link']}\n\n")

    print(f"Scraped {len(results)} items and saved to olx_car_cover_results.txt")

if __name__ == "__main__":
    scrape_olx_car_cover()
