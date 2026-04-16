fields = {
    "AI": ["machine learning", "deep learning", "neural", "ai"],
    "Materials Science": ["material", "nanoparticle", "semiconductor"],
    "Spintronics": ["spin", "magnetic"],
    "Networks": ["network", "communication", "wireless"],
}

def classify(title):
    title = title.lower()

    for field, keywords in fields.items():
        for k in keywords:
            if k in title:
                return field

    return "Other"