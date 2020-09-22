FROM python:3.7.9-alpine3.12

RUN pip install flask flask_cors xmltodict json2xml

WORKDIR /home/

ADD flaskserver4.py .
ADD cert.pem .
ADD key.pem .

COPY data/ data/
COPY wadl/ wadl/

EXPOSE 5004

CMD python3 flaskserver4.py