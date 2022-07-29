# pull the official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
CMD apt-get -y update
CMD apt-get -y install vim nano
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
# copy entrypoint.sh
COPY ./docker-entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/docker-entrypoint.sh
RUN chmod +x /usr/src/app/docker-entrypoint.sh
# copy project
COPY . /usr/src/app

EXPOSE 8000
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]