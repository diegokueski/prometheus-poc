# These are the necessary import declarations
#from opentelemetry import metrics

from random import randint
from flask import Flask, jsonify
from prometheus_client import start_http_server
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

if __name__ == '__main__':
    resource = Resource(attributes={
        SERVICE_NAME: "flask-metrics-example"
    })
    # Start Prometheus client
    start_http_server(port=8000, addr="0.0.0.0")

    # Initialize PrometheusMetricReader which pulls metrics from the SDK
    # on-demand to respond to scrape requests
    reader = PrometheusMetricReader()
    provider = MeterProvider(
        resource=resource, 
        metric_readers=[reader]
    )
    metrics.set_meter_provider(provider)

    #custom
    meter = metrics.get_meter(__name__)

    counter = meter.create_counter(
        name="requests", unit="count", description="The number of requests the app has had"
    )

    dicevalue = meter.create_histogram(
        name="dice_value", unit="s", description="Value of the dice rolls"
    )

    app = Flask(__name__)

    @app.route("/rolldice")
    def roll_dice():
        #return str(do_roll())
        return {
            "result": do_roll()
        }

    @app.route("/rolldicehistogram")
    def roll_dice_gauge():
        roll_value = do_roll()
        dicevalue.record(roll_value, {"environment": "staging"})
        return {
            "result": roll_value
        }

    def do_roll():
        res = randint(1, 6)
        # This adds 1 to the counter for the given roll value
        counter.add(1, {"environment": "staging"})
        return res
    
    @app.route('/health')
    def health():
        return {'result': 'healthy'}
    
    #Prometheus client (http_server) requires the debug is turn off
    app.run(debug=False, host='0.0.0.0', port=5000)
