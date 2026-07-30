from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DevOps Monitoring Project!"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "DevOps Monitoring Project"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)