FROM python:3.10-bullseye

WORKDIR /code/app

COPY app /code/app

RUN pip install --no-cache-dir --upgrade poetry
RUN poetry install

CMD ["gunicorn", "--conf", "app/gunicorn_conf.py", "--bind", "127.0.0.1:8001"]