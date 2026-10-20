from flask import Flask, jsonify, request
from utils import format_response, validate_input

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify(format_response("Welcome to DevSecOps P5 API", 200))

@app.route("/api/check", methods=["POST"])
def check_data():
    data = request.get_json() or {}
    text = data.get("text", "")
    if not validate_input(text):
        return jsonify(format_response("Invalid input", 400)), 400
    return jsonify(format_response(f"Processed: {text}", 200))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
