PREFIX="basic-"
REPOS="flask-app" "sanic-app"

NO_COLOR=\033[0m
GREEN=\033[32;01m
RED=\033[31;01m
YELLOW=\033[33;22m

check-env:
ifndef PROJECTS_HOME
	$(error PROJECTS_HOME environment variable is not set.)
endif
	@ printf "\n[${YELLOW} PROJECTS_HOME set to ${PROJECTS_HOME} ${NO_COLOR}]\n"

update: check-env
	@ printf "\n[${YELLOW} Updating/Cloning repos in ${PROJECTS_HOME} ${NO_COLOR}]\n"
	@ for r in ${REPOS}; do \
		echo "(${PREFIX}$${r})"; \
		if [ ! -e ${PROJECTS_HOME}/${PREFIX}$${r} ]; then \
			git clone git@github.com:dcdarrell9/${PREFIX}$${r}.git ${PROJECTS_HOME}/${PREFIX}$${r}; \
		else \
			cd ${PROJECTS_HOME}/${PREFIX}$${r}; \
			echo "On branch [`git symbolic-ref --short HEAD`], updating repo..."; \
			git pull; cd; \
		fi; echo ""; \
	done

lint:
	pipenv run flake8
	pipenv check ./basic_flask_app ./tests

test: lint
	pipenv run pytest

start:
	@ printf "\n[${YELLOW} Bringing up docker compose ${NO_COLOR}]\n"
	docker-compose up --no-deps

build: check-env
	@ printf "\n[${YELLOW} Refreshing build ${NO_COLOR}]\n"
	docker-compose build
