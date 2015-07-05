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
├── application
│   ├── __init__.py
│   └── routes.py
├── templates
│   └── base.html
└── tests
│   ├── __init__.py
│   └── test_app.py
├── config.py
├── requirements.txt
├── run.py
├── run.sh
├── test.sh
└── README.md
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
