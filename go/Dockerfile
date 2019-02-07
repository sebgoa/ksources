FROM golang:alpine AS builder

COPY . /go/src/ksource
WORKDIR /go/src/ksource

RUN apk update && apk add --no-cache git openssh-client ca-certificates
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o /go/bin/ksource

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/bin/ksource /go/bin/ksource

ENTRYPOINT ["/go/bin/ksource"]
