# Makefile for Dropcam Python Module.
#
#
# Author:: Greg Albrecht <gba@onbeep.com>
# Copyright:: Copyright 2014 OnBeep, Inc.
# License:: Apache License, Version 2.0
# Source:: https://github.com/ampledata/dropcam/
#


.DEFAULT_GOAL := install


install: install_requirements pip_install


install_requirements:
	pip install -r requirements.txt --use-mirrors

pip_install:
	pip install .

uninstall:
	pip uninstall dropcam

develop:
	python setup.py develop

lint:
	pylint -f colorized -i y -r n dropcam/*.py tests/*.py *.py

flake8:
	flake8 --max-complexity 12 dropcam/*.py tests/*.py *.py

pep8: flake8

clonedigger:
	clonedigger --cpd-output .

publish:
	python setup.py register sdist upload

nosetests:
	python setup.py nosetests

test: install_requirements clonedigger nosetests lint flake8

clean:
	rm -rf *.egg* build dist *.pyc *.pyo cover doctest_pypi.cfg \
	nosetests.xml pylint.log *.egg output.xml flake8.log */*.pyc */*.pyo
