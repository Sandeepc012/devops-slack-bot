import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")
JENKINS_URL = os.environ.get("JENKINS_URL", "http://jenkins:5000")

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json
    if data.get("type") == "url_verification":
        return jsonify({"challenge": data.get("challenge")})
    event = data.get("event", {})
    if event.get("type") == "app_mention":
        channel = event.get("channel")
        trigger_build(channel)
    return "", 200

def trigger_build(channel):
    requests.post(f"{JENKINS_URL}/trigger", json={"channel": channel}, headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}"})

@app.route("/")
def index():
    return "DevOps Slack Bot running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
