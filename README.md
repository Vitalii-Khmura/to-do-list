# to-do-list


A Django project for managing your schedule

## Instalation

Python3 must be already installed

```shell
git clone https://github.com/Vitalii-Khmura/to-do-list.git
python -m venv venv
venv/Scripts/activate
pip innstall requirements.txt

python manage.py runserver
```

Then you should create an ```.env``` file and enter in this file ```SECRET_KEY```

```shell
    SECRET_KEY=<your_secret_key>
```

All Environment variables that should be in ```.env``` file are specified in the ```.env.sample```  file

Finally, perform the migration, write next command in terminal:

```shell
    python manage.py makemigrations
    python manage.py migrate
```

## Features

* Create task
* Mark the task as completed or not completed
* Add tag for your task (ex. home, work etc)