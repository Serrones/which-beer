test:
	pytest -v

lint:
	python -m flake8

format:
	black .

fix-import:
	isort .