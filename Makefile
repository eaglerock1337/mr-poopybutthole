VERSION = 0.8

all: stop build

stop:
	docker stop mr-poopybutthole

build:
	docker build --tag mr-poopybutthole:${VERSION} .
	docker run -d --rm --name mr-poopybutthole mr-poopybutthole:${VERSION}

