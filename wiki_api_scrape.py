import wikipediaapi

def scrape_wikipedia_search(topic, max_entries=200):
    user_agent = "MyWikiScraper/1.0"
    wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)

    search_results = wiki_wiki.page(topic, unquote=True).links

    entries = {}
    count = 0

    for page in search_results.values():
        if count >= max_entries:
            break

        page_title = page.title
        page_text = page.text

        if page_title not in entries:
            entries[page_title] = page_text
            count += 1

    return entries

if __name__ == "__main__":
    selected_topic = "Machine Learning"
    max_entries = 100

    entries = scrape_wikipedia_search(selected_topic, max_entries)

    # Print the titles of the scraped entries
    for i, title in enumerate(entries.keys(), 1):
        print(f"{i}. {title}")

    # Optionally, save the entries to a JSON file
    import json
    with open('wikipedia_entries.json', 'w', encoding='utf-8') as json_file:
        json.dump(entries, json_file, ensure_ascii=False, indent=4)
