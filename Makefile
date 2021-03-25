VERSION = $(shell python3 -c "import mr_poopybutthole as mpb; print(mpb.__version__)")

all: stop build

stop:
	docker stop mr-poopybutthole

build:
	docker build --tag mr-poopybutthole:${VERSION} .
	docker run -d --rm --name mr-poopybutthole mr-poopybutthole:${VERSION}
