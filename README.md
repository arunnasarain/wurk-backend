# Venv

- Even though we have docker setup, we use venv for things like migrations
- Install venv `pip install virtualenv`
- Navigate to the project directory and run `python3 -m venv .venv`
- Activate the venv by running `source .venv/bin/activate`
---

## Django App

- Create new app(basically microservice) using `python manage.py startapp <app_name>`
- It will create a directory with some predefined files. Add the new app in `wurk_backend/setting.py` in `installed_apps` list. Configure url as well.
- Write handler function in `views.py`.
- Write db configuration in `models.py`. Create a class and define the table elements. It is very eay in django to deal with database. Do all table declaration, later you can also update. Django will take care of reflecting it into table.
- Run `python3 manage.py makemigrations` to create migration file. Then run `python3 manage.py migrate` to reflect changes into database

---

## Docker configuration

- Make sure docker is installed by running `docker version` and `docker-compose version` in Terminal or install docker and docker-compose.
- Just run `docker-compose up`
- Service is running in `port 8000` and exposed to `3000`
- Postgres is running in `port 5432` and exposed `3001`. So if for any reason you want to access docker database outside, use `psql -h localhost -p 8001 -Upostgres -d wurk` 
---