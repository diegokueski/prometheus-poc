
## Deploy service
kubectl apply -k .

## Test service
kubectl port-forward svc/nginx -n nginx 8080:80
http://localhost:8080/

## Test metrics
kubectl port-forward svc/nginx -n nginx 9113:9113
http://localhost:9113/metrics
