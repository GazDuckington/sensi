include .env
test:
	poetry run pytest

build:
	poetry build

publish:
	poetry config http-basic.pypi ${PYPI_USERNAME} ${PYPI_TOKEN}
	poetry publish
