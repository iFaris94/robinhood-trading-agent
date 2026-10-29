"""Paper-only market monitoring service. Requires a licensed/authorized quote feed."""
import os, time, threading, logging
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
lock = threading.Lock()
state = {'mode':'paper','trading_enabled':False,'market_feed_connected':False,'last_check':None,'last_price':None,'signal':'none','errors':[]}
POLL_SECONDS = max(10,int(os.getenv('POLL_SECONDS','30')))
# This application deliberately does not accept or expose brokerage credentials.
# No invented quotes, and no live orders.
def worker():
    while True:
        with lock:
            state['last_check'] = datetime.now(timezone.utc).isoformat()
            state['signal'] = 'waiting_for_authorized_market_data'
        time.sleep(POLL_SECONDS)

@app.get('/')
def index():
    with lock: return jsonify(dict(state))

@app.get('/health')
def health():
    return jsonify(status='ok', mode='paper', trading_enabled=False)

if __name__ == '__main__':
    threading.Thread(target=worker,daemon=True).start()
    app.run(host='0.0.0.0',port=int(os.getenv('PORT','10000')))
else:
    threading.Thread(target=worker,daemon=True).start()
