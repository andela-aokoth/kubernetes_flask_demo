FROM python:3.5-alpine

RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/

WORKDIR /usr/src/app/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]

EXPOSE 8000
