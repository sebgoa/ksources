FROM debian:7-slim

RUN apt-get update && \
    apt-get install -y curl

ADD event-binary.sh /event.sh

ENTRYPOINT ["/event.sh"]
