from random import randint
from flask import Flask, request

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route("/rolldice")
    def roll_dice():
        return str(do_roll())

    def do_roll():
        return randint(1, 10)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
