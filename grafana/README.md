# Grafana

## Access to grafana  
```kubectl port-forward svc/my-kube-prometheus-stack-grafana 3000:80```  
http://localhost:3000/
http://localhost:3000/datasources/edit/prometheus/dashboards (prometheus dashboards)

## Metric query
Raw query
container_cpu_usage_seconds_total{namespace!="kube-system"}

## Export
You can export the dashbord as a json file

## Import
You can import the exported json file
