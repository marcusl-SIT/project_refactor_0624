FROM python:3.12-alpine
RUN apk update && apk add build-base

EXPOSE 5001/tcp
WORKDIR /app
RUN mkdir static
RUN pip install pandas seaborn flask

COPY data.csv .
COPY app.py .

CMD [ "python", "./app.py" ]
