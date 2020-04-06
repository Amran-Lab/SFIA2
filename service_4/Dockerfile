FROM python:alpine3.11

RUN mkdir /opt/SFIA2/

COPY . /opt/SFIA2/

WORKDIR /opt/SFIA2/
RUN apk add --update \
  && pip3 install --upgrade pip

RUN pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

ENTRYPOINT ["python3", "app.py"]