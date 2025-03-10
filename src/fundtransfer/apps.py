from django.apps import AppConfig


class FundtransferConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundtransfer'

    def ready(self):
        import fundtransfer.signals 