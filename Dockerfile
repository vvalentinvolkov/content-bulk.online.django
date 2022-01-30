FROM python:3.10-bullseye

WORKDIR /code

COPY ./app /code/app

RUN pip install --no-cache-dir --upgrade poetry
RUN poetry config virtualenvs.create false ; poetry install

ENTRYPOINT ["cd", "app"]
CMD ["gunicorn", "--conf", "app/gunicorn_conf.py"]