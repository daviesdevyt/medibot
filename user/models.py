from django.contrib.auth.models import AbstractUser

from utils.models import BaseAbstractModel


# Create your models here.
class User(AbstractUser, BaseAbstractModel):
    pass
