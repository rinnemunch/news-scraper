from scraper import get_headlines

headlines = get_headlines()

print("\nTop Headlines:\n")
for i, (title, link) in enumerate(headlines[:5], 1):
    print(f"{i}. {title}\n   {link}\n")
