import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get('https://www.opm.gov/json/operatingstatus.json')

    return render_template("hello.html", data=response.json())

if __name__ == "__main__":
    app.run()
