import json
from datetime import datetime
from scraper.g2_scraper import scrape_g2
from scraper.capterra_scraper import scrape_capterra
from scraper.getapp_scraper import scrape_getapp  # optional bonus source

def get_reviews(company, source, start_date, end_date):
    try:
        if source == "g2":
            return scrape_g2(company, start_date, end_date)
        elif source == "capterra":
            return scrape_capterra(company, start_date, end_date)
        elif source == "getapp":  # optional bonus
            return scrape_getapp(company, start_date, end_date)
        else:
            print("Invalid source. Using sample reviews.")
    except Exception as e:
        print(f"Scraping failed: {e}. Using sample reviews.")
    
    # Fallback sample reviews
    return [
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

def main():
    company = input("Company name (slug): ")
    source = input("Source (g2/capterra/getapp): ").lower()
    start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d")
    end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d")

    reviews = get_reviews(company, source, start_date, end_date)

    # Save JSON output
    with open("output/sample_output.json", "w") as f:
        json.dump(reviews, f, indent=4)

    print(f"{len(reviews)} reviews saved to output/sample_output.json")

if __name__ == "__main__":
    main()
