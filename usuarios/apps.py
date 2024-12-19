from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'


    def ready(self):
        import usuarios.signals        #registrando o signals no (app usuarios).(arquivo signals.py)
