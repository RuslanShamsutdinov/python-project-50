install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
check:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
run:
	gendiff file3.json file4.json --format stylish
run2:
	gendiff file3.json file4.json --format plain
run3:
	gendiff file3.json file4.json --format json