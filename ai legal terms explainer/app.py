from flask import Flask, render_template, request
from backend1 import GenerateResponse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = GenerateResponse(user_input)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)