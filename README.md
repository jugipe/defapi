# Delivery Fee Calculator - Backend
Wolt Summer 2023 Engineering Internships\
Preliminary Assignment for Engineering Positions\
Backend

## Deployments
The API is up and running in Heroku, you can test it with the url:

    * https://delivery-fee-api.herokuapp.com/


## Description
A single endpoint HTTP API which calculates the delivery fee based on the information in the request payload and includes the calculated delivery fee in the response payload.\
\
The application calculates the delivery fee according to the instructions in this repo https://github.com/woltapp/engineering-summer-intern-2023.


### Built with
* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)


## Getting started
To get your local copy up and running follow these steps. The instructions assume that you have a working python interpreter on your local machine

### With Docker
If you want to run the project locally I suggest running it in [Docker](https://www.docker.com/) /

1. If you don't have docker, follow the instructions in the website for installation
2. Navigate to wanted folder and unpack the provided zip there
 ```sh
 tar -xf defapi-main.zip
 ```
3. After unzip run
 ```sh
  docker-compose up -d
 ```
4. And you can test the API at @ http://localhost:8000/

### Without docker
If you want to run the project without docker I suggest using a virtual environment these instructions apply to debian based systems

1. Install the virtual environment
 ```sh
 sudo apt-get install -y python3-venv
 ```
2. Create the virtual environment
 ```sh
 python3 -m venv /path/to/directory
 ```
3. Head to the virtual environment
 ```sh
 cd /path/to/venv
 ```
4. Activate the virtual environment
 ```sh
 . bin/activate
 ```
5. Unpack the provided zip there
 ```sh
 tar -xf defapi-main.zip
 ```
6. Install the required depencies
 ```sh
 pip install -r requirements.txt
 ```
7. Head to src and run the tests to check that everything is ok
 ```sh
 cd src/ && Python3 -m pytest -v
 ```
8. In the src folder start the api
 ```sh
 uvicorn api:app --host 0.0.0.0 --port 8000
 ```
9. And you can test the API at @ http://localhost:8000/


## Usage
 When the api is up and running I suggest testing it with [Postman](https://www.postman.com/)\
 You can also test it with curl\
 ```sh
 curl -X POST http://localhost:8000/ -H 'Content-Type: application/json' -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}'
 ```
 The API will return
 ```sh
 {"delivery_fee": 710}
 ```

## Contact
Jukka Pelli - jukka.pelli@tuni.fi