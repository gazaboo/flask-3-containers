# Containerized application qui sert un e-page HTML
# HTML -> formulaire enregistrement utilisateur
# Returns all data from database

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({
        "name": "florian",
        "lastname": "Dadouchi"
    })


if __name__ == '__main__':
    print("----------------> users")
    app.run(host="0.0.0.0", debug=True)
