# Million Factories Testing

## Table of Contents

<!-- MarkdownTOC -->

- [Briefing](#briefing)
- [How-to](#how-to)
  - [Preinstall](#preinstall)
  - [Generate million objects](#generate-million-objects)
  - [Run server](#run-server)

<!-- /MarkdownTOC -->

---

## Briefing

This repo aim to benchmark the performance of GeoDjango with million objects for Disfactory project.

## How-to

### Preinstall

- `pipenv`
- `postgis`
- `postgres`

### Generate million objects

- `pipenv run python millionfactory/manage.py migrate`
- `pipenv run python millionfactory/manage.py generate_factories 1000000`

### Run server

- `pipenv run python millionfactory/manage.py collectstatic`
- `cd millionfactory && pipenv run gunicorn -w 3 --access-logfile - --reload millionfactory.wsgi`
