## Loki

## Install loki with promtail
```
helm repo add loki https://grafana.github.io/loki/charts
helm repo update
helm upgrade --install loki loki/loki-stack
```
+ Loki service
http://loki:3100

+ Loki querys
```
{app="flask-example",container="flask-example"} |= `rolldice`
rate({app="flask-example"} |= ``[60s])
count_over_time({app="flask-example"} |= ``[60s])
```


## References
- https://cylab.be/blog/197/deploy-loki-on-kubernetes-and-monitor-the-logs-of-your-pods
- https://www.youtube.com/watch?v=XHexyDqa_S0&t=979s
- https://medium.com/nerd-for-tech/logging-at-scale-in-kubernetes-using-grafana-loki-3bb2eb0c0872 
