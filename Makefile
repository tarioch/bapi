test:
	pipenv run py.test

prepare:
	pip install pipenv --upgrade

init:
	pipenv install --dev --skip-lock 

.PHONY: install test
