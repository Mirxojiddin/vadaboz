from django.apps import AppConfig


class PromiseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'promise'

    def ready(self):
        import promise.signals