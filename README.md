# Cookiecutter Django Hexagonal Architecture

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), inspired by [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django), Cookiecutter Django Hexagonal Architecture is a framework for quickly driving production-ready Django projects using hexagonal architecture.

## Features

- For Django 4.2
- Works with Python 3.10
- [12-Factor](https://12factor.net) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Docker support using [docker-compose](https://github.com/docker/compose) for development

## Usage

Let's pretend you want to create a Django project called "redditclone". Rather than using startproject and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter to do all the work.

First, get Cookiecutter. Trust me, it's awesome:

```
pip install "cookiecutter>=1.7.0"
```

Now run it against this repo:

```
cookiecutter https://github.com/serivt/cookiecutter-django-hexagonal-architecture
```

Enter the project and take a look around, and create a git repo and push it there:

```
cd reddit/
ls
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:pydanny/redditclone.git
git push -u origin main
```
