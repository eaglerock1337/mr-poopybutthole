VERSION = 0.3

all: build

build:
	docker stop mr-poopybutthole
	docker build --tag mr-poopybutthole:${VERSION} .
	docker run -d --rm --name mr-poopybutthole mr-poopybutthole:${VERSION}

