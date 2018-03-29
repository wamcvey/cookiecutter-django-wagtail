from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.core'
    verbose_name = "Core"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import core.signals  # noqa F401
        except ImportError:
            pass