from flask import Flask
from flask import Flask
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)  


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Welcome to DevOps Monitoring Project what ya!"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "DevOps Monitoring Project"
    }

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)