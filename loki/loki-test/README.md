
# Build docker image
```
docker build -t loki-test:latest .
docker run -p 5000:5000 loki-test:latest 
```

# Deploy in k8s cluster
```
kubectl apply -k .k8s
kubectl port-forward svc/loki-test -n loki-test 5000
http://localhost:5000/info
```

# Show logs
```
kubectl logs -n loki-test loki-test-85696c4b57-227dq
```

# Grafana query
```
{app="loki-test"}
{app="loki-test"}|= "ERROR"
# This format allow filter using json fields
{app="loki-test"} | json | level="DEBUG"
# Filter with regex
{app="loki-test"} | json | message=~ ".*log 1.*" | level="ERROR"
```