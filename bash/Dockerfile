FROM debian:7-slim

RUN apt-get update && \
    apt-get install -y curl

ADD event.sh /event.sh

ENTRYPOINT ["/event.sh"]
