# Containerized application qui sert un e-page HTML
# HTML -> formulaire enregistrement utilisateur
# Returns all data from database

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    users = requests.get("http://back-users:5000").json()
    meteo = requests.get("http://back-meteo:5000").json()
    answer = users["name"] + " " + meteo["temperature"]
    return answer


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
