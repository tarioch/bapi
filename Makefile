test:
	pipenv run py.test --junitxml=report.xml

prepare:
	pip install pipenv --upgrade

init:
	pipenv install --dev --skip-lock 

.PHONY: install test
