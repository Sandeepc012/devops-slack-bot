from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/trigger", methods=["POST"])
def trigger():
    channel = request.json.get("channel", "")
    return jsonify({"status": "started", "channel": channel})

@app.route("/")
def index():
    return "Jenkins simulator"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
