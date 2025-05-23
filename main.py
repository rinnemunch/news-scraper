from scraper import get_headlines
import csv


def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(headlines)
    print(f"✅ Saved to {filename}")


def main():
    print("📰 Welcome to News Scraper!")

    try:
        limit = int(input("How many headlines do you want to fetch? (e.g., 5): "))
    except ValueError:
        print("Invalid number. Defaulting to 5.")
        limit = 5

    headlines = get_headlines()

    print(f"\nTop {limit} Headlines:\n")
    for i, (title, link) in enumerate(headlines[:limit], 1):
        print(f"{i}. {title}\n   {link}\n")

    export = input("Export to CSV? (y/n): ").strip().lower()
    if export == "y":
        save_to_csv(headlines[:limit])


if __name__ == "__main__":
    main()
