# Prometheus

## Install prometheus

- Start minikube cluster
```minikube start -p prometheus-poc```

- Install Prometheus and Grafana
This intallation has completed integration between prometheus and grafana.

```helm install my-kube-prometheus-stack prometheus-community/kube-prometheus-stack``` 

- Get credentials
```kubectl get secret my-kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo``` 
admin/prom-operator

- Access to grafana  
```
kubectl port-forward svc/my-kube-prometheus-stack-grafana 3000:80
```  
http://localhost:3000/
http://localhost:3000/datasources/edit/prometheus/dashboards (prometheus dashboards)

- Access to prometheus dashboard  
```kubectl port-forward svc/my-kube-prometheus-stack-prometheus 9090```  
http://localhost:9090/

- Access to kube-state-metrics
kubectl port-forward svc/my-kube-prometheus-stack-kube-state-metrics 8080
http://localhost:8080/metrics


## References
- straightforward installation (Prom and Graf)
https://www.macstadium.com/blog/how-to-k8s-getting-started-with-prometheus-and-grafana

- Grafana configurarion
https://opensource.com/article/21/6/chaos-grafana-prometheus
