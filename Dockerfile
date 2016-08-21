

FROM python:3.5.2-alpine
MAINTAINER Regner Blok-Andersen <shadowdf@gmail.com>

ADD main.py /app/
ADD requirements.txt /app/

WORKDIR /app/

RUN pip install -qU pip \
&& pip install -r requirements.txt

CMD python main.py