#!/bin/sh

export DJANGO_SETTINGS_MODULE="empty.settings"

sphinx-build -a -n -E -b html -d ../django-formwizard/docs/build/doctrees ../django-formwizard/docs/ .

