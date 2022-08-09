FROM python:3.8-slim AS requirements

# preparing requirements
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

FROM python:3.8-slim

# prepare environment
COPY --from=requirements /tmp/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /code
COPY ./mr_poopybutthole mr_poopybutthole
COPY ./.env .env
COPY ./mr-poopybutthole.py mr-poopybutthole.py
ENV DEV_MODE="False"

CMD python mr-poopybutthole.py
