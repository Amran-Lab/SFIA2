FROM python:3

RUN mkdir /opt/SFIA2/

COPY . /opt/SFIA2/

WORKDIR /opt/SFIA2/


RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "app.py"]