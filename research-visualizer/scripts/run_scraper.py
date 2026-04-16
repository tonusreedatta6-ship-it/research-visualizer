from backend.database import insert_data

sample_data = [
    ("Deep Learning for AI", "AI", "Andrew Ng", "Stanford"),
    ("Neural Networks Study", "AI", "Geoffrey Hinton", "Toronto"),
    ("Quantum Materials Research", "Materials Science", "John Smith", "MIT"),
    ("Wireless Networks Optimization", "Networks", "Jane Doe", "Stanford"),
]

def run():
    for title, field, researcher, uni in sample_data:
        insert_data(title, field, researcher, uni)
        print("Inserted:", title)

run()
print("Done!")