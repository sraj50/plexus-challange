MODULE := app

init:
	python setup.py install

venv-unix:
	python3 -m venv venv

venv-windows:
	py -3.8 -m venv venv

run:
	@python -m $(MODULE) $(ARGS)

test:
	@pytest
