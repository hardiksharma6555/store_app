from flask import Flask, render_template, jsonify, request
from api.resource import User, api

app = Flask(__name__)

api.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
