MODULE := app

init:
	python setup.py install

venv:
	python3 -m venv venv

run:
	@python -m $(MODULE) $(ARGS)

test:
	@pytest
