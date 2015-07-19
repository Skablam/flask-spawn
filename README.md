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
│   ├── views.py
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

### Add Views

The -v or --view option allows the quick addition of views, by view it means a
a route that displays a templates. So with the option a new route is added that renders a new template.

```
spawn new anotherapp -v hello
```
This above command creates an app called anotherapp and adds a route /hello that renders a template called hello.html.

This option can be used multiple times to create many views:
```
spawn new anotherapp -v hello -v login -v logout
```

### Adding a Data View

If you are building an api then you don't want to render a template, so option
-dv or --dataview adds a route that returns a Response class.
```
spawn new anotherapp -dv goodbye
```
The above command creates an app called anotherapp and adds a view /goodbye.

This option can be used multiple times to create many routes:
```
spawn new anotherapp -dv goodbye -dv ciao -dv adios
```

### Add Templates

The option -t or --template adds a template to the templates folder.
```
spawn new anotherapp -t hithere
```
The above commands adds a template called hithere.html.

This option can also be used multiple times:
```
spawn new anotherapp -t hithere -t how -t are -t you
```
