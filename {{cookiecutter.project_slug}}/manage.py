#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from {{cookiecutter.project_slug}}.shared.infrastructure.django.management.utility import ManagementUtility


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.shared.infrastructure.django.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    utility: ManagementUtility = ManagementUtility(sys.argv)
    utility.execute()


if __name__ == "__main__":
    main()
