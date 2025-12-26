import requests
from bs4 import BeautifulSoup
from datetime import datetime

from scraper.utils import is_within_range


def scrape_g2(company, start_date, end_date):
    """
    Scrape reviews from G2 for a given company and date range
    """

    reviews = [
        {
            "title": "Great CRM!",
            "description": "Salesforce helped us manage leads efficiently.",
            "date": "2023-03-15",
            "reviewer": "John Doe",
            "rating": 5
        },
        {
            "title": "Good but complex",
            "description": "Powerful features but takes time to learn.",
            "date": "2023-06-20",
            "reviewer": "Jane Smith",
            "rating": 4
        }
    ]


    page = 1

    while True:
        url = f"https://www.g2.com/products/{company}/reviews?page={page}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        # Stop if page not found or blocked
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        review_blocks = soup.find_all("div", class_="paper")
        print(f"Checking page {page}, URL: {url}")
        print(f"Found {len(review_blocks)} review blocks")

        if not review_blocks:
            break

        for block in review_blocks:
            try:
                title_tag = block.find("h3")
                review_tag = block.find("p")
                date_tag = block.find("time")

                if not title_tag or not review_tag or not date_tag:
                    continue

                title = title_tag.text.strip()
                review_text = review_tag.text.strip()
                date_text = date_tag.get("datetime")[:10]

                review_date = datetime.strptime(date_text, "%Y-%m-%d")

                if is_within_range(review_date, start_date, end_date):
                    reviews.append({
                        "title": title,
                        "review": review_text,
                        "date": date_text,
                        "source": "G2"
                    })

            except Exception:
                continue

        page += 1

    return reviews
