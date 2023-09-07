# Music

## Description

The logic of the project is divided into 3 main parts, a car dealership, car suppliers, and a buyer. The car dealership buys cars from the supplier, then the car is sent to the buyer from the car dealership. All possible discounts at each of the sublevels are taken into account.

## How to run

Create virtual env:

```
python -m venv .venv
```
Configure environment variables:

```
cp .env.sample .env
```

Start services

```
docker-compose build
```

Apply migrations

```
docker-compose run app python manage.py migrate
```

Start app

```
docker-compose up
```
