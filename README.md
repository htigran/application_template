# PYTHON TEMPLATE APPLICATION

[![Build Status](https://travis-ci.org/tigranza/python_app_template.svg?branch=master)](https://travis-ci.org/tigranza/python_app_template)  [![Coverage Status](https://coveralls.io/repos/github/tigranza/python_app_template/badge.svg?branch=master)](https://coveralls.io/github/tigranza/python_app_template?branch=master)

## SCOPE
This is a python application template that can be used out of the box. It comes with inbuilt argument parser, configuration file parser and a log handler.
The idea is to have minimalistic starting point while implementing similar python applications.

## FUNCTIONAL REQUIREMENTS
- [x] Shell get config file path via command line arguments
- [x] Shell parse and load given confignfile
- [x] Shell get log file path from given config file
- [x] Shell log output in given log file
- [x] Shell read log level from given config file
- [x] Shell filter out log entries with log level less than specified in the config file

## NON FUNCTIONAL REQUIREMENTS
- [x] Shell be minimalistic
- [x] Shell work out of the box

## DESIGN

## USAGE
### git
1) Clone the github repository
1) Remove .git
1) git init with your own remote

### build
~~~~
make venv - creates a virtual environment and installs requirements
make test - runs unit tests and code analysis
make vim - exports PYTHONPATH, activates virtual environment and opens a vim
make run - runs the application
~~~~

## REFERENCES
