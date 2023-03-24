# Flask example

## Run local using prometheus exporter

´´´
flask run
´´´
http://127.0.0.1:5000/rolldice
http://127.0.0.1:5000/rolldicehistogram
http://localhost:8000/metrics

## Docker
´´´
docker build -t flask-example:latest .
docker run -p  8000:8000 -p 5001:5001 flask-example:latest

flask run --port=5001
flask --app /usr/app/app.py run  &

http://localhost:5000/rolldice
http://localhost:8000/metrics
´´´

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