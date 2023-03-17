# Flask example

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


## References
https://opentelemetry.io/docs/instrumentation/python/getting-started/