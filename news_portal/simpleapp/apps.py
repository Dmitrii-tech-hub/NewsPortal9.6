from django.apps import AppConfig

class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'

    def ready(self):
        import simpleapp.signals  # Ensure signals are loaded
        # No need for start_scheduler if you're using Celery



