install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_main.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install format lint test format