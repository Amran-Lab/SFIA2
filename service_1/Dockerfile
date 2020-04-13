FROM python:alpine3.11

RUN mkdir /opt/SFIA2/

COPY . /opt/SFIA2/

WORKDIR /opt/SFIA2/
RUN apk add --update \
  && pip3 install --upgrade pip

RUN pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;
RUN apk add mariadb-dev \
    && pip3 install Flask-MySQLdb

ENTRYPOINT ["python3", "app.py"]