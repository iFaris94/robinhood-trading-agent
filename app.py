"""Read-only service scaffold; no broker integration or live trading."""
import os
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def status():
    return jsonify(service='robinhood-trading-agent', mode='scaffold', trading_enabled=False)

@app.get('/health')
def health():
    return jsonify(status='ok', timestamp=datetime.now(timezone.utc).isoformat())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '10000')))
