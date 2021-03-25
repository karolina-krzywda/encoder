FROM python:3.7.9-alpine
EXPOSE 8000
COPY . /app
WORKDIR /app
RUN apk update && apk add gcc build-base
RUN pip install -r requirements.txt
CMD ["python","main.py"]
