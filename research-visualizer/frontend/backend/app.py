from flask import Flask, jsonify, request
from backend.database import get_data_by_university
import random

app = Flask(__name__)

@app.route("/search")
def search():
    uni = request.args.get("university")

    # Get data from database
    data = get_data_by_university(uni)

    # If no data found, generate fallback data
    if not data:
        fields = ["AI", "ML", "Networks", "Data Science"]

        data = {
            f: random.randint(5, 20)
            for f in fields
        }

    return jsonify({
        "university": uni,
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True)