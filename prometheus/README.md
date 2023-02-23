
## Access to prometheus dashboard

```kubectl port-forward svc/my-kube-prometheus-stack-prometheus 9090```  
http://localhost:9090/

## Metric query
kube_pod_container_resource_requests{container="coredns"}


