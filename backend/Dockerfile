# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /src
ADD ./src /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY /src/requirements.pip .
RUN pip install -r /src/requirements.pip

# copy project
COPY . .

CMD python manage.py migrate