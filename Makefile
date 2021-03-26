VERSION = $(shell python3 -c "import mr_poopybutthole as mpb; print(mpb.__version__)")

start: build run
all: restart
restart: stop build run

stop:
	docker stop mr-poopybutthole

build:
	docker build --tag mr-poopybutthole:${VERSION} .

run: 
	docker run -d --rm --name mr-poopybutthole mr-poopybutthole:${VERSION}

log:
	docker logs -f mr-poopybutthole | tee mr-poopybutthole.log

env:
	pip install pipenv
	pipenv install --dev

local:
	pipenv run python mr-poopybutthole.py

test:
	@echo "Not done yet!"

lint:
	black .
