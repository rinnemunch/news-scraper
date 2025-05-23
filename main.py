from scraper import get_headlines
import csv


def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(headlines)
    print(f"✅ Saved to {filename}")


def save_to_txt(headlines, filename="headlines.txt"):
    with open(filename, mode="w", encoding="utf-8") as file:
        for i, (title, link) in enumerate(headlines, 1):
            file.write(f"{i}. {title}\n   {link}\n\n")
    print(f"✅ Saved to {filename}")


def main():
    print("📰 Welcome to News Scraper!")

    try:
        limit = int(input("How many headlines do you want to fetch? (e.g., 5): "))
    except ValueError:
        print("Invalid number. Defaulting to 5.")
        limit = 5

    headlines = get_headlines()
    keyword = input("Filter headlines by keyword? (press Enter to skip): ").strip().lower()

    filtered = [
        (title, link)
        for (title, link) in headlines
        if keyword in title.lower()
    ] if keyword else headlines

    print(f"\nTop {limit} Headlines" + (f" matching '{keyword}'" if keyword else "") + ":\n")
    for i, (title, link) in enumerate(filtered[:limit], 1):
        print(f"{i}. {title}\n   {link}\n")

    export_format = input("Export format? (csv/txt/none): ").strip().lower()

    if export_format == "csv":
        save_to_csv(filtered[:limit])
    elif export_format == "txt":
        save_to_txt(filtered[:limit])
    else:
        print("🛑 No export selected.")


if __name__ == "__main__":
    main()
