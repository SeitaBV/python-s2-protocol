.PHONY: tests
SHELL := /bin/bash

generate-models:
	source venv/bin/activate && datamodel-codegen --input s2-ws-json/s2-asyncapi/s2-cem.yaml --input-file-type openapi  --output src/python_s2_protocol/

install-for-dev:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt && pip install -e .

test:
	source venv/bin/activate && pytest