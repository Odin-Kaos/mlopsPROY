.PHONY: install lint format test refactor all run-api run-cli

VENV := .venv
PY := $(VENV)/bin/python
UV := uv

install:
	# Create venv and sync dependencies from uv.lock / pyproject.toml
	$(UV) venv $(VENV)
	$(UV) sync

lint:
	$(UV) run pylint Lab1 || true

format:
	$(UV) run black mylib api cli tests

test:
	$(UV) run pytest -v --cov=Lab1

refactor: format lint

all: install format lint test

run-api:
	fastapi dev api/api.py

run-cli:
	$(UV) run python -m Lab1.cli.cli
