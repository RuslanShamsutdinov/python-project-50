### Hexlet tests and linter status:
[![Actions Status](https://github.com/RuslanShamsutdinov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/RuslanShamsutdinov/python-project-50/actions)
[![Python CI](https://github.com/RuslanShamsutdinov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/RuslanShamsutdinov/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/699a525b8a4e3cb3f397/maintainability)](https://codeclimate.com/github/RuslanShamsutdinov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/699a525b8a4e3cb3f397/test_coverage)](https://codeclimate.com/github/RuslanShamsutdinov/python-project-50/test_coverage)

### Difference Calculator
***
Difference Calculator compares old and changed files and shows a difference.  
Types of compared files: 

    - JSON
    - YAML  

Result is displayed in the formats:

    - stylish  (default)
    - plain
    - json

Setup using Makefile:

    1. make install
    2. make build
    3. make package-install

Utility usage:

    gendiff <file_path1> <file_path2> --format <format>

Help: 

    gendiff -h

Minimum requirements:
- python = ">=3.8.1,<4.0" 

JSON file comparison("stylish" default formatter key):

<a href="https://asciinema.org/a/tONuzE08FhOJwyNm7NP5Tx9h5" target="_blank"><img src="https://asciinema.org/a/tONuzE08FhOJwyNm7NP5Tx9h5.svg" /></a>

YAML file comparison("stylish" default formatter key):

<a href="https://asciinema.org/a/mZl8WB8F99NYpJzHCzZM3WC06" target="_blank"><img src="https://asciinema.org/a/mZl8WB8F99NYpJzHCzZM3WC06.svg" /></a>

Сompare files with formatter key "stylish":

<a href="https://asciinema.org/a/0n7yKMVDne67wVymzFQZZbTdm" target="_blank"><img src="https://asciinema.org/a/0n7yKMVDne67wVymzFQZZbTdm.svg" /></a>

Сompare files with formatter key "plain":

<a href="https://asciinema.org/a/X5Hu5uHMJPv9x94atJF7G87Sm" target="_blank"><img src="https://asciinema.org/a/X5Hu5uHMJPv9x94atJF7G87Sm.svg" /></a>

Сompare files with formatter key "json":

<a href="https://asciinema.org/a/M6GE3OcHgqDDFuXZSKGKPILOo" target="_blank"><img src="https://asciinema.org/a/M6GE3OcHgqDDFuXZSKGKPILOo.svg" /></a>