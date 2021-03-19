# Setup
- install python 3.9: Download Python | Python.org
- make sure pip is updated: `python3 -m pip install --upgrade pip`
- install auto virtual env handler: `pip3 install pipenv`
- enter virtual env: `pipenv shell`
- install dependencies: `pipenv install`
- configure flask app:
```
  export FLASK_APP=app
  export FLASK_ENV=development
  flask run
```