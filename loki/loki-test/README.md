
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
{app="loki-test"} | json | level="DEBUG" | message > 80

# Filter with regex
{app="loki-test"} | json | message=~ ".*log 1.*" | level="ERROR"

# Logs that doesn't have some word
{app="loki-test"} != "error"
{app="loki-test"} |= "error" != "log 0" # Exclude logs with log 0 string 

#Format log title
{app="loki-test"} | json | level="DEBUG" | line_format "{{.level}} {{.message}}"

# Add new label using existing value
{app="loki-test"} | label_format magic_field=app | json | level="DEBUG" 
{app="loki-test"} | json | level="DEBUG" | label_format magic_field=level
```

## Grafana charts
```
count_over_time({app="loki-test"}|="ERROR"[5s])

```

## Queries references
- https://grafana.com/docs/loki/latest/logql/log_queries/