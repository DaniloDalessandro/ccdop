from django.apps import AppConfig

class ContractConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contract'

class ContractConfig(AppConfig):
    name = 'contract'

    def ready(self):
        import contract.signals
