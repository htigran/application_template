

.PHONY: run
VENV_DIR := venv
ACTIVATE := $(VENV_DIR)/bin/activate
PIP      := $(VENV_DIR)/bin/pip

run:
	test -f $(ACTIVATE) \
	    && source $(ACTIVATE); \
	    python application/my_app.py -c application/config/my_app.conf

venv:
	sudo yum install -y python-virtualenv
	rm -fr $(VENV_DIR)
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

