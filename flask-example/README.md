# Flask example

## Run local using prometheus exporter

´´´
flask run
´´´
http://127.0.0.1:5000/rolldice
http://127.0.0.1:5000/rolldicehistogram
http://localhost:8000/metrics


## Run in k8s

+ Start minikube cluster
´´´
minikube start -p prometheus-poc
´´´

+ Deploy to k8s
´´´`
kubectl apply -k .k8s
´´´

+ Test
´´´
kubectl run mycurlpod --image=curlimages/curl -i --rm --tty -- sh
curl http://flask-example.flask-example.svc.cluster.local:5000/health
curl http://flask-example.flask-example.svc.cluster.local:8000/metrics
´´´

## Add metrics to prometheus
+ Reference
https://youtu.be/mLPg49b33sA?t=799

+ Check de prometheus console
´´´
kubectl port-forward svc/my-kube-prometheus-stack-prometheus 9090
http://localhost:9090/
´´´

+ Add the servicemonitor k8s resource (mandatory to prometheus scraping)
´´´
The servicemonitor requires to use the same label that prometheus has config to scrap (my-kube-prometheus-stack in my case).
This is the magit to register a new servicemonitor in prometheus.
metadata:
  labels:
    release: my-kube-prometheus-stack
´´´

## Docker
´´´
docker build -t flask-example:latest .
docker run -p  8000:8000 -p 5001:5001 flask-example:latest

flask run --port=5001
flask --app /usr/app/app.py run  &

http://localhost:5000/rolldice
http://localhost:8000/metrics
´´´
---

## Local setup
´´´
pipenv install -r requirements.txt
pipenv shell
´´´

´´´
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    flask run
´´´
http://127.0.0.1:5000/rolldice

++Show the metrics
http://localhost:8000/metrics

´´´
opentelemetry-instrument \
    --traces_exporter console \
    flask run
´´´

## References
https://opentelemetry.io/docs/instrumentation/python/getting-started/