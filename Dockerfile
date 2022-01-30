FROM python:3.10-bullseye

WORKDIR /code/app

COPY ./app /code/app
COPY ./pyproject.toml /code
COPY ./poetry.lock /code

RUN pip install --no-cache-dir --upgrade poetry
RUN poetry config virtualenvs.create false ; poetry install

CMD echo hello