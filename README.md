# Basic Setup
- install homebrew in your preferred method: https://docs.brew.sh/Installation
- install mongodb locally: https://docs.mongodb.com/manual/administration/install-community/
- install python 3.9: Download Python | Python.org
- make sure pip is updated: `python3 -m pip install --upgrade pip`

# Project Setup
- install auto virtual env handler: `pip3 install pipenv`
- enter virtual env: `pipenv shell`
- install dependencies: `pipenv install`
- configure flask app local variables:
`export FLASK_APP=app`
`export FLASK_ENV=development`
- start mongod in the background: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#run-mongodb-community-edition
- start the application: `flask run`