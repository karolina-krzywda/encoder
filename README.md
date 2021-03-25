### How to run the app?
1. From root directory build docker image with command:
docker build -t app .
2. After build phase start container with command:
docker run -d -p 8000:8000 app

App is up and running on localhost port 8000 

To encode text use endpoint:
localhost:8000/encode/TEXT_TO_ENCODE
where TEXT_TO_ENCODE should be replaced with text to encode

To decode text use endpoint:
localhost:8000/decode/TEXT_TO_DECODE

### App to encode and decode uses cesar cipher
