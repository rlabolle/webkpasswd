FROM python:alpine
MAINTAINER Romain Labolle <romain.labolle@universite-lyon.fr> 

RUN apk upgrade --no-cache && \
    apk add --no-cache krb5-libs ca-certificates curl && \
    addgroup -S gunicorn && \
    adduser -S -h /var/lib/gunicorn -G gunicorn -g "Gunicorn" -s /bin/ash -D gunicorn

WORKDIR /app
COPY pyproject.toml /app/
COPY webkpasswd /app/webkpasswd
RUN apk add --no-cache --virtual .build-dependencies krb5-dev gcc libc-dev python3-dev && \
    pip install --no-cache-dir .[krb] && \
    apk del --no-cache .build-dependencies && \
    rm -Rf /app/

USER gunicorn
WORKDIR /var/lib/gunicorn
EXPOSE 8000/tcp
HEALTHCHECK --interval=5s --timeout=3s CMD curl --silent --show-error --fail http://localhost:8000/healthz || exit 1
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "webkpasswd:app"]
