# AstraDot

## Getting Started

Create and activate a Python virtual environment if you haven't already:

```
virtualenv venv
. venv/bin/activate
```
(Technically you don't **HAVE** to, but it's a super good idea.)


You can set APP_CONFIG environment variables:
```
export APP_CONFIG=development
```

In the config file replace SQLALCHEMY_DATABASE_URI replacing placeholders with your credentials

```
mysql+pymysql://<user>:<pass>@localhost:3306/astradot
```
Start up a Python shell and initialize your database:

```
echo 'db.create_all()' | ./manage.py shell
```

Start up Flask's local development server:

```
./manage.py runserver
```

Use the API's I specified in the Postman collection
