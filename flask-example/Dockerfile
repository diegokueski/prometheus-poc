FROM alpine:3.17 AS builder

#Add bash to the image
RUN apk add --no-cache py3-pip python3 bash
RUN apk add build-base linux-headers
RUN apk add curl

COPY requirements.txt /usr/app/
WORKDIR /usr/app/
RUN pip3 install -r requirements.txt

#Add new stage
FROM builder AS finisher

# Create a group and user
RUN addgroup -S appuser && adduser -S appuser -G appuser

COPY --chown=appuser:appuser . /usr/app/
RUN chmod u+x /usr/app/entrypoint.sh

EXPOSE 5000
EXPOSE 8000

USER appuser
ENTRYPOINT ["/usr/app/entrypoint.sh"]
