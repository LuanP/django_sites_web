lint:
	flake8 --exclude=migrations,settings.py src/

test:
	make lint && make coverage

coverage:
	coverage run --source='./src' src/manage.py test

report:
	coverage report

install:
	pip install -r requirements/production.txt

install-development:
	pip install -r requirements/development.txt
	cp .hooks/pre-commit .git/hooks/
	cp .hooks/pre-push .git/hooks/
