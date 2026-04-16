from scholarly import scholarly
from backend.classifier import classify
from backend.database import insert_data

def scrape_author(name, university):
    print("Scraping:", name)

    try:
        search = scholarly.search_author(name)
        author = next(search, None)

        if not author:
            print("Author not found")
            return

        author = scholarly.fill(author)

        pubs = author.get('publications', [])

        for pub in pubs[:10]:
            try:
                bib = pub.get('bib', {})
                title = bib.get('title', None)

                if not title:
                    continue

                field = classify(title)
                insert_data(title, field, name, university)

            except Exception as e:
                print("Skipping one paper:", e)
                continue

        print("Done scraping!")

    except Exception as e:
        print("Main error:", e)