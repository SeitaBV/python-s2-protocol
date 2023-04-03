.PHONY: tests
SHELL := /bin/bash

generate-models:
	source generate_models.sh
	
install-for-dev:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt && pip install -e .

test:
	source venv/bin/activate && pytest