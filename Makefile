-include .env
export

run:
	@python django_project/manage.py runserver

startapp:
	@python django_project/manage.py startapp ${app_name}