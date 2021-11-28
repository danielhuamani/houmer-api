# Challenge for houm

## Installation

First step clone .env.template with .env

For installation it is necessary to have two terminals.

#### First terminal

let's install dynamodb.

Build dynamodb

```
docker-compose build
```

Run dynamodb


```
docker-compose up
```

#### Second terminal

for install is necessary to have node > 14


install serverless global

```
npm install -g serverless

```

install dependencies

```
npm install
```


install pipenv

```
pip install pipenv
```

create environment

```
pipenv shell
```

install requirements

```
pipenv install
```

run flask

```
sls wsgi serve -p 8002
```

## Important rules to understand the project

To calculate the time in the property, I assume that the person send coordinate  when enters property and also send coordinate  when leaves property.

How do I calculate if the person enters o leaves the property?

When the person sends their coordinate I verify the last record of the date:

- If not exist record is because the first property to visit so I create a record.
- If exist a record I compare the last coordinate with the now coordinate if the difference in the distance in mt2 is less than mt2(MT2_MAX in .env) allowed I assume that the person  leaves the property so updated the record with the end coordinate.
- If exist a record I compare the last coordinate with the now coordinate if the difference in the distance in mt2 is higher than mt2(MT2_MAX in .env) allowed I assume that the persona visit a new property so I create a new record.

But if the persona doesn't send the coordinate when leaves the property I couldn't calculate how long he was in the property.