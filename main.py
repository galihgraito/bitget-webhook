from flask import Flask, request

app = Flask(__name__)

# Endpoint buat nerima sinyal dari TradingView
@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Webhook received:", data)
    return '✅ Webhook received', 200

# Endpoint buat test di browser
@app.route('/', methods=['GET'])
def index():
    return "🚀 Webhook bot is live!", 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
