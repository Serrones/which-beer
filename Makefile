test:
	pytest -v

lint:
	python -m flake8
	isort --check .

format:
	black .

fix-import:
	isort .

install:
	poetry install

build-container:
	docker build -t which-beer .

run-container:
	docker run -it -v ~/Downloads:/app/files/ --rm --name beer which-beer bash
