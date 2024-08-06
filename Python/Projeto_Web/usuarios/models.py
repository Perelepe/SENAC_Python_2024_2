from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = "E-mail do Usuário",
        max_length = 100,
        unique = True,
    )
