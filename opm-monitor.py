import requests
import json

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get('https://www.opm.gov/json/operatingstatus.json')

    data = response.json()

    posted_date = data['DateStatusPosted']
    opm_title = data["Title"]
    opm_location = data["Location"]
    opm_status_summary = data["StatusSummary"]

    return render_template("hello.html",
                           opm_title=opm_title,
                           opm_location=opm_location,
                           opm_status_summary=opm_status_summary,
                           posted_date=posted_date)

if __name__ == "__main__":
    app.run()
