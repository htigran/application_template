

.PHONY: run
VENV_DIR := venv
ACTIVATE := $(VENV_DIR)/bin/activate
PIP      := pip
INSTALLER:= $(shell python -mplatform | grep -qi centos && echo "yum install -y" || echo "apt-get --assume-yes install")
SHELL    := /bin/bash

run:
	@$(call activate-venv, \
	    $@, \
	    "python application/my_app.py -c application/config/my_app.conf")

venv:
	sudo $(INSTALLER) python-virtualenv
	virtualenv $(VENV_DIR)
	source $(ACTIVATE) \
	    && $(PIP) install --upgrade setuptools \
	    && $(PIP) install -r requirements.txt  \
	    && $(PIP) install -r test-requirements.txt

test: unit-tests coverage pylint

unit-tests:
	@$(call activate-venv, \
	    $@, \
	    "PYTHONPATH=`pwd`/application nosetests tests/common/")

coverage:
	@$(call activate-venv, \
	    $@, \
	    "coverage run application/my_app.py -c application/config/my_app.conf; \
	     coveralls")

pylint:
	@$(call activate-venv, \
	    $@, \
	    "pylint application/common")

clean:
	rm -fr venv logs


vim:
	@$(call activate-venv, \
	    $@, \
	    "PYTHONPATH=`pwd`/application vim")


.PHONY: vim venv run

define activate-venv
	mkdir -p logs; \
	test -f $(ACTIVATE) \
	    && source $(ACTIVATE); \
	    echo "-----------------------------$(1)-----------------------------------"; \
	    eval "$(2)"
endef
