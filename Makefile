lint:
	flake8 --exclude=migrations,settings.py,test_settings.py src/

test:
	make lint && make coverage

coverage:
	export DJANGO_SETTINGS_MODULE="django_sites_web.test_settings" && cd src/ && coverage run --source='.' --omit='**/tests.py' manage.py test && cp .coverage ..

report:
	coverage report

install:
	pip install -r requirements/production.txt

install-development:
	pip install -r requirements/development.txt
	cp .hooks/pre-commit .git/hooks/
	cp .hooks/pre-push .git/hooks/
