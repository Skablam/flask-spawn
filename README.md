# flask-spawn
Generate new flask applications quickly and easily, in a variety of customisable structures.


## Quickstart

To begin:

```
pip install flask-spawn
```

To create a new flask application use the following command:

```
spawn new nameofapp
```

This will create an application with the following structure:

```
nameofapp
├── README.md
├── application
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── base.css
│   │   ├── images
│   │   └── js
│   └── templates
│       └── base.html
├── tests
│    ├── __init__.py
│    └── test_app.py
├── config.py
├── requirements.txt
├── run.py
├── run.sh
└── test.sh
```

Then install python libraries (it is recommnded that you do this inside a virtualenv):

```
pip install -r requirements.txt
```
Then your app is good to go. Run with:

```
source run.sh
```
The basic unit test structure has also been setup. Run the tests:

```
source test.sh
```

## Easy Customisations

### Add Model and Database Migrations

The -d or --database option adds the files and code necessary to do alembic migrations via flask-migrate.

```
spawn new anotherapp -d
```
This would create a new flask application called anotherapp with the same structure as seen in the Quickstart section above but with a manage.py and a models.py as well as the necessary config, imports and  requirements.

Once done it would be a matter of updating the SQLALCHEMY_DATABASE_URI config to point at the right database (assuming it has been created) and updating the models.py to the required structure and then running the following lines of code to update the database structure:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
