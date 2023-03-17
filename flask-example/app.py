# These are the necessary import declarations
from opentelemetry import metrics

from random import randint
from flask import Flask, request

# Acquire a meter.
meter = metrics.get_meter(__name__)

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)

@app.route("/rolldice")
def roll_dice():
    return str(do_roll())

def do_roll():
    res = randint(1, 6)
    # This adds 1 to the counter for the given roll value
    roll_counter.add(1, {"roll.value": res})
    return res
