from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "👋 Welcome to the User Service!"

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.args.get("user", "Guest")
    return jsonify(message=f"🚀 Welcome, {user}! You're inside the CI/CD pipeline.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
