from pathlib import Path

from django.conf import settings
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        app_name = options.pop("name")
        target: Path | str = options.pop("directory") or settings.BASE_DIR
        if target == settings.BASE_DIR:
            target = settings.BASE_DIR / Path(app_name)
            if not target.exists():
                target.mkdir()
        options["template"] = options["template"] or ".app_template"
        super().handle("app", app_name, target, **options)
