-include .env
export

run:
	@python django_project/manage.py runserver

startapp:
	@python django_project/manage.py startapp ${app_name}

makemigrations:
	@python django_project/manage.py makemigrations

migrate:
	@python django_project/manage.py migrate

superuser:
	@python django_project/manage.py createsuperuser