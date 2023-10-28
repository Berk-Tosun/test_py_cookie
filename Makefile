PYTHON = venv/bin/python

init:
	$(PYTHON) -m pip install --upgrade pip wheel pre-commit
	$(PYTHON) -m pip install --upgrade -r requirements.txt -r requirements_dev.txt --editable .
	pre-commit install --hook-type pre-commit --hook-type commit-msg

update: update-deps update-dev-deps init

update-deps:
	$(PYTHON) -m pip install --upgrade pip pip-tools
	$(PYTHON) -m piptools compile --upgrade -o requirements.txt pyproject.toml

update-dev-deps:
	$(PYTHON) -m pip install --upgrade pip-tools pip wheel pre-commit
	pre-commit autoupdate
	$(PYTHON) -m piptools compile -o requirements_dev.txt pyproject.toml --extra dev --extra doc --extra test --upgrade -c requirements.txt

clean:
	pre-commit uninstall -t pre-commit -t commit-msg
	pre-commit clean
	rmdir -rf venv

bump:
	cz bump
	# push-tag

fetch-tags:
	git fetch --tags

push-tag: fetch-tags
	git push --follow-tags origin main

test-coverage: venv
	pytest --cov=src --cov-report=html:docs/cov

.PHONY: init update update-deps update-dev-deps test-coverage bump fetch-tags push-tag
