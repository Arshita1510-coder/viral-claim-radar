from flask import Flask, request, jsonify
from flask_cors import CORS
from fact_checker import analyze_claim
from database import save_claim, get_history

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    claim = data.get("claim")

    result = analyze_claim(claim)

    save_claim(claim, result) 

    return jsonify(result)


@app.route("/history", methods=["GET"])
def history():

    data = get_history()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)