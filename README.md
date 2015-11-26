# README for hemedicinal

TODO: verify that the following info is correct:

 - Python:  3.4
 - DB:      PostgreSQL (locally SQLite or optionally PostgreSQL)

**Create virtualenv**

 `virtualenv --python=python3.4 venv`

 `. ./venv/bin/activate`

or if you use virtualenvwrapper

 `mkvirtualenv hemedicinal`

 `workon hemedicinal`

**Install dependencies**

 `pip install -r requirements/local.txt`

**Switch to internal dir**

 `cd hemedicinal`

**Create local settings**

Create settings/local.py from settings/local.py.example, if you want to use PostgreSQL locally uncomment and add the database details there.

**Syncdb & migrate**

 `python manage.py syncdb`

 `python manage.py migrate`

**Run development servers**

**Note:** Virtualenv must be activated for the following commands to work

Run django server: `python manage.py runserver`

**Note:** Server will run at 127.0.0.1:8000 (localhost wont work because of CORS)

