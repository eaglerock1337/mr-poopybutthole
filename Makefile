VERSION = $(shell python3 -c "import mr_poopybutthole as mpb; print(mpb.__version__)")

.PHONY: default
default: help

# generate help info from comments: thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## help information about make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: build run ## ALIAS: build, run

.PHONY: restart
restart: stop build run ## ALIAS: stop, build, run

.PHONY: stop
stop: ## stop the Docker container
	docker stop mr-poopybutthole

.PHONY: build
build: ## build the bot's Docker image
	docker build --tag mr-poopybutthole:${VERSION} .

.PHONY: run
run: ## run the bot inside Docker
	docker run -d --rm --name mr-poopybutthole mr-poopybutthole:${VERSION}

.PHONY: log
log: ## display the Docker container's logs and save to a logfile
	docker logs -f mr-poopybutthole | tee mr-poopybutthole.log

.PHONY: env
env: ## set up a local development environment
	pip install pipenv
	pipenv install --dev

.PHONY: local
local: ## run the bot locally
	pipenv run python mr-poopybutthole.py

.PHONY: dev
dev: ## run the bot locally in development mode
	pipenv run python mr-poopybutthole.py --dev

.PHONY: test
test: ## run pytest unit tests
	@echo "Not done yet!"

.PHONY: lint
lint: ## lint all code with black
	black .
