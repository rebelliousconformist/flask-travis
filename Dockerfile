
FROM python:3-alpine

RUN apk add --update py3-pip
RUN pip3 install --upgrade pip

COPY ./requirements.txt ./usr/app/requirements.txt

WORKDIR /usr/app

RUN pip3 install -r requirements.txt

CMD ["python3","files/app.py"]