### REST API (FastAPI) written in Python to encode and decode messages.
1). Messages are encoded and decoded using cesar cipher with 4-digit shift.

2). Authentication is required to access api (Basic Auth).

3). Api returns responses in JSON format.

### How to run the app?
1. From root directory build docker image with command:
docker build -t app .
2. After build phase start container with command:
docker run -d -p 8000:8000 app

App is up and running on localhost port 8000 

To encode text use endpoint:
localhost:8000/encode/TEXT_TO_ENCODE,
where TEXT_TO_ENCODE should be replaced with text to encode

To decode text use endpoint:
localhost:8000/decode/TEXT_TO_DECODE

#### To access endpoints use predefined user and password:
user: user
password: secret123
