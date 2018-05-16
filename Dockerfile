FROM alpine:3.7
MAINTAINER Romain Labolle <romain.labolle@universite-lyon.fr> 

RUN apk upgrade --no-cache && \
    apk add --no-cache krb5-libs python3 ca-certificates curl && \
    pip3 install --upgrade pip && \
    addgroup -S gunicorn && \
    adduser -S -h /var/lib/gunicorn -G gunicorn -g "Gunicorn" -s /bin/ash -D gunicorn

COPY requirements.txt /tmp/
RUN apk add --no-cache --virtual .build-dependencies krb5-dev gcc libc-dev python3-dev && \
    pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apk del --no-cache .build-dependencies

COPY app /var/lib/gunicorn
RUN chown -R gunicorn:gunicorn /var/lib/gunicorn

USER gunicorn
WORKDIR /var/lib/gunicorn
EXPOSE 8000/tcp
HEALTHCHECK --interval=5s --timeout=3s CMD curl --silent --show-error --fail http://localhost:8000/healthz || exit 1
CMD ["/usr/bin/gunicorn", "-b", "0.0.0.0:8000", "app:app"]
