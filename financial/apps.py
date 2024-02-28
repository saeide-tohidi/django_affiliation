from django.apps import AppConfig


class FinancialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "financial"
    verbose_name = "وضعیت مالی کاربران"

    def ready(self):
        import financial.signals
