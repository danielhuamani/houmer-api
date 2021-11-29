# Challenge for houm


## Set ENVIROMENT

First step create .env from .env.template, after set variables for mode local you should set:

- MODE=LOCAL -> this variable is necessary to use dynamodb
- DYNAMODB_PORT=8000 -> it use for connect with dynamo docker 
- STAGE=dev -> stage
- REGION=us-east-2 -> region of aws
- MT2_MAX=100 -> This variable is very important because it helps determine the maximum m2 that the person can walk and send coordinates within the property

## Important rules to understand the project

To calculate the time in the property, I assume that the person send coordinate  when enters property and also send coordinate  when leaves property.

How do I calculate if the person enters o leaves the property?

When the person sends their coordinate I verify the last record of the date:

- If not exist record is because the first property to visit so I create a record.
- If exist a record I compare the last coordinate with the now coordinate if the difference in the distance in mt2 is less than mt2(MT2_MAX in .env) allowed I assume that the person  leaves the property so updated the record with the end coordinate.
- If exist a record I compare the last coordinate with the now coordinate if the difference in the distance in mt2 is higher than mt2(MT2_MAX in .env) allowed I assume that the persona visit a new property so I create a new record.

But if the persona doesn't send the coordinate when leaves the property I couldn't calculate how long he was in the property.

## Installation



### First terminal

let's install dynamodb.

Build dynamodb

```bash
docker-compose build
```

Run dynamodb


```bash
docker-compose up
```

### Second terminal

for install is necessary to have node > 14


install serverless global

```bash
npm install -g serverless
```

install dependencies

```bash
npm install
```


install pipenv

```bash
pip install pipenv
```

create environment

```bash
pipenv shell
```

install requirements

```bash
pipenv install
```

run flask

```bash
sls wsgi serve -p 8002
```


## Unit Test

```bash
pytest
```


## Deploy

before deployment you should change variable MODE=PROD in .env

```bash
sls deploy
```


## Demo API


### Register coordinates
method: POST 

Api: https://qn11tlev33.execute-api.us-east-2.amazonaws.com/dev/houmer/{houmerID}/coordinates

body:
```json
{
 "longitude": {float},
 "latitude": {float}
}
```

### Get visits by date
method: GET 

Api: https://qn11tlev33.execute-api.us-east-2.amazonaws.com/dev/houmer/{houmerID}/{date:iso8610}/visit


### Get speed by date

method: GET 

Api: https://qn11tlev33.execute-api.us-east-2.amazonaws.com/dev/houmer/{houmerID}/{date:iso8610}/speed

GET params:

    speed: {float:optional}
