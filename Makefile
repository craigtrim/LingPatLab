# -------------------------------------------------------------
#  Project: spaCy Core
# -------------------------------------------------------------
ifeq ($(OS),Windows_NT)
	os_shell := powershell
	download_spacy_model := .\resources\scripts\Download-Spacy-Model.ps1
else
	os_shell := bash
	poetry_remove_lib := resources/scripts/poetry_remove_lib.sh
	download_spacy_model := ./resources/scripts/download_spacy_model.sh
endif

# Download the Spacy model
get_model:
	$(os_shell) $(download_spacy_model)

test:
	poetry run pytest

build:
	make get_model
	poetry lock
	poetry check
	poetry update
	poetry build
	poetry install

regress:
	poetry run python regression/regression_runner.py

all:
	make build
	make test
