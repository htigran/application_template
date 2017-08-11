

.PHONY: run
VENV_DIR := venv
ACTIVATE := $(VENV_DIR)/bin/activate
PIP      := $(VENV_DIR)/bin/pip
INSTALLER:= $(shell python -mplatform | grep -qi centos && echo "yum install -y" || echo "apt-get --assume-yes install")
SHELL    := /bin/bash

run:
	rm test.log
	test -f $(ACTIVATE) \
	    && source $(ACTIVATE); \
	    python application/my_app.py -c application/config/my_app.conf
	cat test.log

venv:
	sudo $(INSTALLER) python-virtualenv
	virtualenv $(VENV_DIR)
	source $(ACTIVATE) \
	    && $(PIP) install -r requirements.txt \
	    && $(PIP) install -r test-requirements.txt

test:
	@test -f $(ACTIVATE) \
	    && source $(ACTIVATE); \
	    echo -e "--------------------------coverage------------------------------------\n"; \
	    coverage run application/my_app.py -c application/config/my_app.conf; \
	    coveralls; \
	    echo -e "--------------------------nosetests-----------------------------------\n"; \
	    nosetests application/tests/common/; \
	    echo -e "-----------------------------pylint-----------------------------------\n"; \
	    pylint application/common; \
	    echo -e "----------------------------------------------------------------------\n";



.PHONY: venv run

