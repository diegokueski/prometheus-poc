
docker run --entrypoint /bin/bash  -it nginx
docker run -p 8080:8080 nginx

docker build -t nginx-custom:latest .
docker run -p 8080:80 nginx-custom:latest