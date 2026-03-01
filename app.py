from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

events = []

@app.route("/")
def home():
    html = """
    <h2>GitHub Webhook Events</h2>
    <ul>
    {% for event in events %}
        <li>{{event}}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, events=events)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event", "unknown")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    events.append(f"{event_type} event received at {timestamp}")

    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run(debug=True)
