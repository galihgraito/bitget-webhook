from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook is live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received Webhook:", data)
    return "Received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
