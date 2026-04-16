import requests
from backend.database import insert_data

def fetch():
    url = "https://api.openalex.org/works?search=machine learning&per-page=30"

    res = requests.get(url)
    data = res.json()

    results = data.get("results", [])

    universities = [
        "University of Toronto",
        "MIT",
        "Stanford University",
        "Harvard University"
    ]

    fields = ["AI", "ML", "Data Science", "Networks"]

    i = 0

    for item in results:
        title = item.get("title")
        if not title:
            continue

        insert_data(
            title,
            fields[i % len(fields)],
            "OpenAlex Author",
            universities[i % len(universities)]
        )

        i += 1

    print("Done inserting balanced dataset")

fetch()