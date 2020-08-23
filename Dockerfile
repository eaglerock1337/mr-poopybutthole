FROM python:3.8-slim

# preparing requirements
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

# prepare environment
RUN pip install -r /tmp/requirements.txt
WORKDIR /code
COPY . .

CMD python mr-poopybutthole.py
