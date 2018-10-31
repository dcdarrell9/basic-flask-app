FROM python:3.7

MAINTAINER darrell.cox

COPY . /app
WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

ENV http_proxy cache2.uk.logica.com:80
ENV https_proxy cache2.uk.logica.com:80

EXPOSE 8080

CMD ["python", "run.py"]
