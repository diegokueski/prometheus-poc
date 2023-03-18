# These are the necessary import declarations
#from opentelemetry import metrics

from random import randint
from flask import Flask, request

# from opentelemetry import metrics
# from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
# from opentelemetry.sdk.metrics import Counter, Meter
# from opentelemetry.sdk.metrics import MeterProvider
# from prometheus_client import start_http_server
from prometheus_client import start_http_server
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})
# Start Prometheus client
start_http_server(port=8000, addr="localhost")
# Initialize PrometheusMetricReader which pulls metrics from the SDK
# on-demand to respond to scrape requests
reader = PrometheusMetricReader()
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)

#custom
meter = metrics.get_meter(__name__)
JOB_COUNTER = meter.create_counter(
    name="jobs_scheduled", unit="count", description="Count of jobs scheduled"
)

#start_http_server(port=8000, addr="localhost")
# Meter is responsible for creating and recording metrics
# metrics.set_meter_provider(MeterProvider())
# meter = metrics.get_meter(__name__)
# # exporter to export metrics to Prometheus
# prefix = "MyAppPrefix"
# exporter = PrometheusMetricsExporter(prefix)
# # Starts the collect/export pipeline for metrics
# metrics.get_meter_provider().start_pipeline(meter, exporter, 5)

# counter = meter.create_counter(
#     "requests",
#     "number of requests",
#     "requests",
#     int,
#     ("environment",),
# )

# Labels are used to identify key-values that are associated with a specific
# metric that you want to record. These are useful for pre-aggregation and can
# be used to store custom dimensions pertaining to a metric
#labels = {"environment": "staging"}

app = Flask(__name__)

@app.route("/rolldice")
def roll_dice():
    return str(do_roll())

def do_roll():
    res = randint(1, 6)
    # This adds 1 to the counter for the given roll value
    #counter.add(25, labels)
    JOB_COUNTER.add(1, attributes={"environment": "staging"})
    return res
