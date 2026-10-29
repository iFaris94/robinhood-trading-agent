# Robinhood Trading Agent

Initial Render deployment scaffold. No brokerage connection, paper-trading simulator, or live order execution is implemented.

Run with `pip install -r requirements.txt && python app.py`.

Render: Python runtime; build `pip install -r requirements.txt`; start `gunicorn app:app` (gunicorn included in requirements).

Endpoints: `/` and `/health`.

Before trading: secure authentication, strategy, paper execution, persistence, idempotency, risk limits, and kill switch must be designed and tested.
