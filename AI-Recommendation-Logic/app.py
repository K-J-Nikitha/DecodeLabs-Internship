from flask import Flask, render_template, request, jsonify
from recommender import get_recommendations

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    category = data.get("category")
    level = data.get("level")

    recommendations = get_recommendations(category, level)

    return jsonify({
        "recommendations": recommendations
    })


if __name__ == "__main__":
   app.run(debug=True, port=5001)
