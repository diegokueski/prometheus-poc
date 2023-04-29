
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

## Aggregation queries
```
#Count the logs every 30 seconds
count_over_time({app="loki-test"} [30s])

#Aggregate the logs by leve every 30 seconds
sum by (level) (count_over_time({app="loki-test"} | json  [30s]))

#The max/min value of the message field every 30s
max_over_time({app="loki-test"} |= "DEBUG" | json | unwrap message [30s])
min_over_time({app="loki-test"} |= "DEBUG" | json | unwrap message [30s])

#Average/Sum the message value every 30 seconds
avg_over_time({app="loki-test"} |= "DEBUG" | json | unwrap message [30s])
sum_over_time({app="loki-test"} |= "DEBUG" | json | unwrap message [30s])

#Aggregate by app
sum by (app) (min_over_time({app="loki-test"} |= "DEBUG" | json | unwrap message [30s]))


```

## Queries references
- https://grafana.com/docs/loki/latest/logql/log_queries/