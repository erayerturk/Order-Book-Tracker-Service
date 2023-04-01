# Order Book Tracker


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

### Notes
This project is created with cookiecutter. "Users" app is not implemented by me.

https://cookiecutter-django.readthedocs.io/en/latest/#

## Basic Commands

### Setting Up
-   To build and up the project, go to local.yml directory and use this command:

        $ docker-compose -f local.yml up --build

-   To create DB tables, use this command:
        
        $ docker-compose -f local.yml run --rm django python manage.py migrate

-   To create a superuser account, use this command:

        $ docker-compose -f local.yml run --rm django python manage.py createsuperuser



#### Running tests with pytest

    $ docker-compose -f local.yml run --rm django pytest

#### Docs (Swagger)
You need to log in to see API documentation. You can use superuser credentials which you created with "createsuperuser" command
    
http://localhost:8000/accounts/login/

http://localhost:8000/api/docs/

### Sample cURL Requests

```
curl --request GET http://localhost:8000/api/order-book-statistics/daily/'
curl --request GET http://localhost:8000/api/order-book-statistics/weekly/'
curl --request GET http://localhost:8000/api/order-book-statistics/monthly/'
```



