test:
	./venv/bin/coverage run -m pytest --ignore=venv
	./venv/bin/coverage report

make venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

make activate:
	source venv/bin/activate