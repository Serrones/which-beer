test:
	pytest -v

lint:
	flake8 --show-source .
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
