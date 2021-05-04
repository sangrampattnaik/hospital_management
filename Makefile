manage=./manage.py
python=python3

runserver:
	$(python) $(manage) runserver

initial-setup: 
	pip install -r requirements.txt

superuser:
	$(python) $(manage) createsuperuser

admin:
	$(python) $(manage) superuser	

test-data:
	$(python) $(manage) test_data

shell:
	$(python) $(manage) shell_plus
	

migrate:
	$(python) $(manage) makemigrations && $(python) $(manage) migrate

freeze:
	pip freeze > requirements.txt