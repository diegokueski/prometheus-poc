# Flask example

## Run local using prometheus exporter

´´´
flaks run
´´´
http://127.0.0.1:5000/rolldice
http://127.0.0.1:5000/rolldicehistogram
http://localhost:8000/metrics

## Local setup
```
pipenv install -r requirements.txt
pipenv shell
```

```
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    flask run
```
http://127.0.0.1:5000/rolldice

++Show the metrics
http://localhost:8000/metrics

opentelemetry-instrument \
    --traces_exporter console \
    flask run

## References
https://opentelemetry.io/docs/instrumentation/python/getting-started/