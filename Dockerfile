FROM python:3.10-bullseye

WORKDIR /code/app

COPY ./pyproject.toml /code
COPY ./poetry.lock /code

RUN pip install --no-cache-dir --upgrade poetry ; \
    poetry config virtualenvs.create false ; \
    poetry install

COPY ./app /code/app

CMD ["gunicorn", "--conf", "gunicorn_conf.py"]