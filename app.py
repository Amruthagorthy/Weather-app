import requests
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/getReport", methods = ["POST"])
def getReport():
    city = request.form["city"]
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=ec9b79c4c63c06534a519841060b102c")
    data = response.json()
    return render_template("report.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)