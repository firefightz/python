from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)


# https://api.genderize.io?name=peter
# {"count":1346866,"name":"peter","gender":"male","probability":1.0}

@app.route('/<name>')
def home(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    stats = response.json()
    return render_template('index.html',
                           count=stats['count'],
                           name=stats['name'],
                           gender=stats['gender'],
                           prob=stats['probability']
                           )


if __name__ == "__main__":
    app.run(debug=True)