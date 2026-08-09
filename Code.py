import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

try:
    print("=" * 55)
    print("             BASIC WEB SCRAPER")
    print("=" * 55)

    print("\nGetting news from BBC...")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Website accessed successfully!")

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all(["h2", "h3"])

    print("\n" + "=" * 55)
    print("              LATEST NEWS HEADLINES")
    print("=" * 55)

    count = 1

    for headline in headlines:
        text = headline.get_text(strip=True)

        if text:
            print(f"{count}. {text}")
            count += 1

        if count > 10:
            break

    if count == 1:
        print("No headlines found.")

except requests.exceptions.RequestException:
    print("\nError: Unable to access the website.")
    print("Please check your internet connection.")

print("\n" + "=" * 55)
print("            Web scraping completed!")
print("=" * 55)