Provisioning a new site

=============================

## Required packages

- nginx
- uwsgi
- Python 3
- Git
- pip
- virtualenv

on Ubuntu :

	sudo apt-get install nginx git python3 python3-pip
	sudo pip install virtualenv uwsgi

## Nginx Virtual Host config

- see staging.aldazar-superlists_nginx.conf
- replace SITENAME by aldazar-superlists.ddns.net

## Uwsgi Worker

- see staging.aldazar-superlists_uwsgi.ini
- replace SITENAME by aldazar-superlists.ddns.net

## Folder structure :

/home/aldazar
|---- sites
	|---- SITENAME
		|---- database
		|---- source
		|---- static
		|---- virtualenv
