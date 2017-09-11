

.PHONY: run
VENV_DIR := ~/.virtualenvs/application
ACTIVATE := $(VENV_DIR)/bin/activate
PIP      := pip
INSTALLER:= $(shell python -mplatform | grep -qi centos && echo "yum install -y" || echo "apt-get --assume-yes install")
SHELL    := /bin/bash
PPATH    := PYTHONPATH=`pwd`/application
PYTHON   := $(PPATH) python

run: venv
	@$(call activate-venv, \
	    $@, \
	    "$(PYTHON) application/main/application.py -c application/config/application.conf")

venv: $(VENV_DIR)
$(VENV_DIR):
	sudo $(INSTALLER) python-virtualenv
	virtualenv $(VENV_DIR)
	source $(ACTIVATE) \
	    && $(PIP) install --upgrade setuptools \
	    && $(PIP) install -r requirements/main.txt  \
	    && $(PIP) install -r requirements/test.txt

test: unit-tests coverage pylint

unit-tests: venv
	@$(call activate-venv, \
	    $@, \
	    "$(PPATH) nosetests -v tests/common/")

coverage: venv
	@$(call activate-venv, \
	    $@, \
	    "$(PPATH) coverage run application/main/application.py -c application/config/application.conf; \
	     coveralls")

pylint: venv
	@$(call activate-venv, \
	    $@, \
	    "pylint application/common application/main")

clean: venv
	rm -fr $(VENV_DIR) logs


vim: venv
	@$(call activate-venv, \
	    $@, \
	    "$(PPATH) vim")


.PHONY: vim venv run

define activate-venv
	mkdir -p logs; \
	test -f $(ACTIVATE) \
	    && source $(ACTIVATE); \
	    echo "-----------------------------$(1)-----------------------------------"; \
	    eval "$(2)"
endef
