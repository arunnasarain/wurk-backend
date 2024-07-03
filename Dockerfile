FROM public.ecr.aws/docker/library/python:3.11

WORKDIR /usr/src/app

COPY ./requirements.txt .

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


RUN python manage.py collectstatic --noinput

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
