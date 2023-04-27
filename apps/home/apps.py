from django.apps import AppConfig
from django.db.models import BigAutoField

class MyAppConfig(AppConfig):
    name = 'apps.home'
    DEFAULT_AUTO_FIELD = BigAutoField
    