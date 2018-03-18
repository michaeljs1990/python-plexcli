install:
	python setup.py install

shell:
	pipenv shell

sync:
	pipenv sync

dev: sync shell
