from django.apps import AppConfig


class AirlinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.directory.airlines'


    def ready(self):
        import apps.directory.airlines.signals
