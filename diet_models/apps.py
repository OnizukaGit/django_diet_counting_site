from django.apps import AppConfig


class DietModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diet_models'


class DietCountingSite(AppConfig):
    name = 'diet_models'

    def ready(self):
        import diet_models.signals
