from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CPFOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(CustomUser.USERNAME_FIELD)

        try:
            # Tente buscar o usuário por email
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            try:
                # Tente buscar o usuário por CPF
                user = CustomUser.objects.get(cpf=username)
            except CustomUser.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
