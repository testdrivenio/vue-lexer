test:
	coverage run --source=vue setup.py test
	flake8 ./vue --ignore=E501
	flake8 ./tests --ignore=E501
	isort ./vue/*.py --check-only
	isort ./tests/*.py --check-only
	black ./vue --check
	black ./tests --check

release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
